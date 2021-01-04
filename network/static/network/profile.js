document.addEventListener("DOMContentLoaded", function () {
    press_edit_review();
    upload_pic();
    return false;
});



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


function upload_pic() {
    document.querySelector("#upload_pic").onsubmit = () => {
        username = document.querySelector("#username").innerHTML;
        image = document.querySelector("#formFileSm").files[0];
        form = new FormData();
        form.append("image", image);
        
        fetch(`/upload_dp/${username}`, {
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

        document.querySelector("#upload_pic").innerHTML = `
            <div class="alert alert-success" role="alert">
                Profile picture uploaded successfully!
            </div>
        `;
        
        setTimeout(() => { window.location = `/profile/${username}` }, 1500);
        
        return false;
    }
}