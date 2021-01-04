
from django.urls import path

from . import views

urlpatterns = [
    # views
    path("", views.login_view, name="login"),
    path("home", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("module/<str:code>", views.view_module, name="view_module"),
    path("profile/<str:username>", views.profile, name="profile"),

    # create new 
    path("new_module", views.new_module, name="new_module"),
    path("new_review/<str:code>", views.new_review, name="new_review"),

    # search
    path("search_code/<str:code>", views.search_code, name="search_code"),
    path("search_name/<str:name>", views.search_name, name="search_name"),

    #API calls
    path("create_module", views.create_module, name="create_module"),
    path("create_review", views.create_review, name="create_review"),
    path("edit_module", views.edit_module, name="edit_module"),
    path("edit_review", views.edit_review, name="edit_review"),
    path("upload_dp/<str:username>", views.upload_dp, name="upload_dp"),
]
