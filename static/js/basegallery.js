var modal = document.getElementById("modal");

var img = document.getElementById("pic");
var modalImg = document.getElementById("pic");
var captionText = document.getElementById("modal-text");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
  modal.style.display = "none";
}