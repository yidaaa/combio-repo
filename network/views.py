from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        identification = request.POST["identification"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username,identification=identification,password=password,email=None)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def new_module(request):
    return render(request, "network/newmodule.html")


@login_required
def new_review(request, code):
    return render(request, "network/newreview.html", {"code": code})

@login_required
def index(request):
    modules = Module.objects.all().order_by('module_code')
    return render(request, "network/index.html", {"modules": modules})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    reviews = Review.objects.all().filter(user=user).order_by('year')
    count = reviews.count()

    paginator = Paginator(reviews, 5)
    if request.GET.get("page") != None:
        try:
            reviews = paginator.page(request.GET.get("page"))
        except:
            reviews = paginator.page(1)
    else:
        reviews = paginator.page(1)

    return render(request, "network/profile.html", {
        "reviews": reviews,
        "total_pages": range(paginator.num_pages),
        "count": count,
    })

@login_required
def view_module(request, code):
    module = Module.objects.get(module_code=code)

    reviews = Review.objects.all().filter(module_code=code).order_by('-year')
    paginator = Paginator(reviews, 5)
    if request.GET.get("page") != None:
        try:
            reviews = paginator.page(request.GET.get("page"))
        except:
            reviews = paginator.page(1)
    else:
        reviews = paginator.page(1)

    return render(request, "network/module.html", {
        "module": module,
        "reviews": reviews,
        "total_pages": range(paginator.num_pages),
    })


@login_required
def search_code(request, code):
    modules = Module.objects.all().filter(module_code__contains=code).order_by('module_code')
    if (modules.count()==0):
        return render(request, "network/index.html", {
            "modules": modules,
            "message": "Your search returned no results. You can create a new module if it has yet to be added in this repository."
        })
    elif (modules.count()==1):
        return view_module(request, code.upper())
    else:
        return render(request, "network/index.html", {"modules": modules})


@login_required
def search_name(request, name):
    modules = Module.objects.all().filter(module_name__contains=name).order_by('module_name')
    print(modules)

    if (modules.count()==0):
        return render(request, "network/index.html", {
            "modules": modules,
            "message": "Your search returned no results. You can create a new module if it has yet to be added in this repository."
        })
    elif (modules.count()==1):
        code = modules.first().module_code
        return view_module(request, code)
    else:
        return render(request, "network/index.html", {"modules": modules})

# API calls
@login_required
def create_module(request):
    if request.method == "POST":
        module_code = request.POST["module_code"]
        module_name = request.POST["module_name"]
        module_summary = request.POST["module_summary"]

        # get all module code
        all_modules = Module.objects.all()
        all_module_codes = [module.module_code for module in all_modules]

        # attempt to create new module
        if (module_code not in all_module_codes):
            module = Module(module_code=module_code, module_name=module_name, module_summary=module_summary)
            module.save()
        else:
            return render(request, "network/newmodule.html", {
                "message": "Module code already exists."
            })

    module = Module.objects.get(module_code=module_code)
    return render(request, "network/module.html", {"module": module})

@csrf_exempt
@login_required
def edit_module(request):
    if request.method == "POST":
        module_summary = request.POST["module_summary"]
        module_code = request.POST["module_code"]
        module = Module.objects.get(module_code=module_code)

        module.module_summary = module_summary
        module.save()
        return JsonResponse({"message": "Edited module summary successfully"}, status=201)
    return JsonResponse({"message": "POST method required"}, status=400)

@login_required
def create_review(request):
    if request.method == "POST":
        user = request.user
        year = request.POST["year"]
        semester = request.POST["semester"]
        professor = request.POST["professor"]
        review = request.POST["review"]
        module_code =  request.POST["module_code"]
        # create new review
        review = Review(user=user, year=year, semester=semester, professor=professor, review=review, module_code=module_code)
        review.save()
        return JsonResponse({"message": "Added review successfully"}, status=201)
    return JsonResponse({"message": "POST method required"}, status=400)

@csrf_exempt
@login_required
def edit_review(request):
    if request.method == "POST":
        review_id = request.POST["review_id"]
        review_text = request.POST["review_text"]

        review = Review.objects.get(id=review_id)
        review.review = review_text
        review.save()
        
        return JsonResponse({"message": "Edited module summary successfully"}, status=201)
    return JsonResponse({"message": "POST method required"}, status=400)

@csrf_exempt
@login_required
def upload_dp(request, username):
    if request.method == 'POST': 
        dp = request.FILES["image"]
        user = User.objects.get(username=username)
        if (user.photo.name != "images/default_image.png"):
            user.photo.delete(save=True)
        user.photo = dp
        user.save()
        return JsonResponse({"message": "Added picture successfully"}, status=201)
    return JsonResponse({"message": "POST method required"}, status=400)