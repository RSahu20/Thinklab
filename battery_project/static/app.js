let cellid;
function uploadImage() {
  var input = document.getElementById("imageInput");
  var file = input.files[0];
  var reader = new FileReader();

  reader.onload = function (event) {
    var img = new Image();
    img.src = event.target.result;
    img.onload = function () {
      var container = document.getElementById("imageContainer");
      var idElement = document.getElementById("imageId");
      var elementId = Math.floor(Math.random() * 9000000000) + 1000000000;
      img.id = elementId;
      cellid = elementId;
      container.style.display = "block";
      container.innerHTML = "";
      container.appendChild(img);
      idElement.innerHTML = "Cell ID: " + elementId;
      let text = cellid;
      JsBarcode("#barcode", text);
      // Display content div after image upload
      document.getElementById("contentDiv").style.display = "block";
    };
  };

  reader.readAsDataURL(file);
}

// Smooth scrolling down to page sections when clicking on navigation links
document.querySelectorAll('header li a').forEach(link => {
  link.addEventListener('click', event => {
    event.preventDefault();
    const targetId = link.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    targetElement.scrollIntoView({ behavior: 'smooth' });
  });
});




// show circuit image on uploading csv file 

const button = document.getElementById("submit-button");
const image = document.getElementById("my-image");

button.addEventListener("click", function() {
  image.style.display = "block";
});