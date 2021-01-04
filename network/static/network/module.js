document.addEventListener("DOMContentLoaded", function () {
    press_review();
    press_edit_summary();
    press_edit_review();
    return false;
});

function press_review() {
    document.querySelector("#create_review_button").onclick = () => {
        code = document.querySelector(".module").id;
        window.location = `/new_review/${code}`;
        return false;
    };
}

// editing summary
function press_edit_summary() {
    document.querySelector("#edit_summary_button").onclick = () => {
        document.querySelector("#edit_summary_button").remove();
        code = document.querySelector(".module").id;
        document.querySelector(".summary").innerHTML = `
        <form id="edit_form">    
            <div>
                <div class="form-group">
                <textarea class="form-control" rows=8 name="summary" id="summary">${document.querySelector("#summary_text").innerHTML.trim()}</textarea>
            </div>
            <input class="btn btn-info" type="submit" value="Submit Edit">
        </form>
        `;

        submit_edit_summary(code);
        return false;
    };
}

function submit_edit_summary(code) {
    document.querySelector("#edit_form").onsubmit = () => {
        text = document.querySelector("#summary").value;
        form = new FormData();
        form.append("module_code", code);
        form.append("module_summary", text);
        
        fetch('/edit_module', {
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

        document.querySelector(".summary").innerHTML = `
            <div class="header"> Summary : </div> 
            <div id="summary_text" >${ text }</div>
            <form>
                <input class="btn btn-info" type="submit" value="Edit Module Summary" id="edit_summary_button">
            </form>
        `; 
        press_edit_summary();
        return false;
    }
}

// editing reviews
function press_edit_review() {
    document.querySelectorAll(".edit_review_button").forEach( button => 
        button.onclick = () => {
            target_element = button.parentElement.parentElement.firstElementChild;
            review_id = button.parentElement.parentElement.id;
            to_edit = target_element.innerHTML;

            target_element.innerHTML = `
            <form id="edit_form">    
                <div>
                    <div class="form-group">
                    <textarea class="form-control" rows=8 name="review" id="edit_review">${to_edit.trim()}</textarea>
                </div>
                <input class="btn btn-secondary btn-sm" type="submit" value="Submit Edit">
            </form>
            `;
            button.remove();
            submit_edit_review(review_id);
            return false;
        })
}

function submit_edit_review(review_id) {
    document.querySelector("#edit_form").onsubmit = () => {
        review_text = document.querySelector("#edit_review").value;
        form = new FormData();
        form.append("review_id", review_id);
        form.append("review_text", review_text);
        
        fetch('/edit_review', {
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

        location.reload();
        return false;
    }
}