document.addEventListener("DOMContentLoaded", function () {
    pressbutton();
    return false;
});

function getCsrf() {
    var inputElems = document.querySelectorAll('input');
    var csrfToken = '';
    for (i = 0; i < inputElems.length; ++i) {
        if (inputElems[i].name === 'csrfmiddlewaretoken') {
            csrfToken = inputElems[i].value;
            break;
        }
    }
    return csrfToken;
};

function pressbutton() {
    document.querySelector("#create_review_form").onsubmit = () => {

        form = new FormData();
        form.append("module_code", document.querySelector(".title").id);
        form.append("year", document.querySelector("#year").value);
        form.append("semester", document.querySelector("#semester").value);
        form.append("professor", document.querySelector("#professor").value);
        form.append("review", document.querySelector("#review").value);
        form.append("csrfmiddlewaretoken", getCsrf() );
        
        fetch('/create_review', {
            method: 'POST',
            body: form,
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
        })
        .catch((error) => {
            console.error(error);
          });
        
        window.location = `/module/${document.querySelector(".title").id}`;
        return false;
    };
}