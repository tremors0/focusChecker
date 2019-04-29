// Add your javascript code here
console.log("IBM Web Starter...");

document.addEventListener("DOMContentLoaded", function(event) {
    document.getElementById("submitImageBtn").addEventListener("click", uploadImage);
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function uploadImage(e) {
    e.preventDefault();
    const files = document.querySelector('[type=file]').files;
    const formData = new FormData();
    const url = "uploadImage";

    if (files == null || files.length === 0) {
        return;
    }

    formData.append('image', files[0]);

    const csrftoken = getCookie('csrftoken');
    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {"X-CSRFToken": csrftoken},
    }).then(response => {
        return response.json();
    }).then(displayResults)
}

function displayResults(response) {
    response.forEach(face => {
        const image = new Image();
        image.src = 'data:image/png;base64,' + face.image;
        document.body.appendChild(image);
        const classes = face.classes;
        classes.forEach(img_class => {
            const dataDiv = document.createElement("div");
            dataDiv.innerText = img_class["class"] + ": " + img_class["score"];
            document.body.appendChild(dataDiv);
        });
    });
}

/**
 *
 * @param {string[]} faces_img base64 string reprezentujici obrazek
 */
function displayImages(faces_img) {
    faces_img.forEach(face => {
        const image = new Image();
        image.src = 'data:image/png;base64,' + face;
        document.body.appendChild(image);
    });
}

