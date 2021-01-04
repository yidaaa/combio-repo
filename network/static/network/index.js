document.addEventListener("DOMContentLoaded", function () {
    click_module();
    search_code();
    search_name();
    return false;
});

function click_module() {
    document.querySelectorAll(".module").forEach(block => {
        block.onclick = () => {
            window.location = `/module/${block.id}`;
            return false;
        };
      });
}

function search_code(){
    document.querySelector("#code_search").onsubmit = () => {
        code = document.querySelector("#code_value").value
        window.location = `/search_code/${code}`;
        return false;
      };
}

function search_name(){
    document.querySelector("#name_search").onsubmit = () => {
        name_value = document.querySelector("#name_value").value
        window.location = `/search_name/${name_value}`;
        return false;
      };
}