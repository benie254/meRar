var modal = document.getElementById("modal");

var pic = document.getElementById("pic");
var modal_pic = document.getElementById("modal-pic");
var modal_text = document.getElementById("modal-text");
pic.onclick = function(){
  modal.style.display = "block";
  modal_pic.src = this.src;
  modal_text.innerHTML = this.alt;
}

var span = document.getElementsByClassName("exit")[0];

span.onclick = function() {
  modal.style.display = "none";
}