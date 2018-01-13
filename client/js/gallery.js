var images = document.getElementsByClassName("image");
var length = images.length;
console.log(length);
images[0].style.left = "20%";
var i = 0;
function moveLeft (){
	// images[0].style.left = "-60%";
	if(i>0)
	{
		images[i].style.left = "-65%";
		images[i-1].style.left = "20%";
		i--;
	}
}
function moveRight (){
	if(i < length - 1){
		images[i].style.left = "100%";
		images[i+1].style.left = "20%";
		i++;
}}
document.addEventListener("keyup", function (event){
	var keyCode = event.keyCode;
	if(keyCode == 39){
		moveRight();
	}
	else if (keyCode == 37){
		moveLeft();
	}
});