
function changeMsg(){
var input = document.theForm.elements[0].value;
document.getElementById("msg").innerHTML=input;
}

function increaseFontSize() {
 document.getElementById("msg").style.fontSize = "400%";
}

function decreaseFontSize() {
 document.getElementById("msg").style.fontSize = "100%";
}

function restoreFontSize() {
 document.getElementById("msg").style.fontSize = "200%";
}

function changeFontStyle() {
 var newFont = document.getElementById("fontMenu").value;
 document.getElementById("msg").style.fontFamily = newFont;
}

function changeColor() {
 newColor=document.getElementById("favcolor").value;
 document.getElementById("msg").style.color = newColor;
}