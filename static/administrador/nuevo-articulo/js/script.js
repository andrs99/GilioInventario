document.getElementById("file").onchange = function(e) {
	let reader = new FileReader();
  
  reader.onload = function(){
    let preview = document.getElementById('preview'),
    image = document.createElement('img');

    image.src = reader.result;
    
    preview.innerHTML = '';
    preview.append(image);
  };
 
  reader.readAsDataURL(e.target.files[0]);
}




var butSelectArea = document.getElementById('btnSelectArea');
var divSelectArea = document.getElementById('despliegueSelectArea');


function showHide(e) {
  e.preventDefault();

  if (divSelectArea.style.display == "none") {
    divSelectArea.style.display = "block";
  } else if (divSelectArea.style.display == "block") {
    divSelectArea.style.display = "none";

  }
  e.stopPropagation();
}

//al hacer click en el boton
butSelectArea.addEventListener("click", showHide, false);

//funcion para cualquier clic en el documento
document.addEventListener("click", function (e) {

  //obtiendo informacion del DOM para  
  // console.log(e.target);
  var clic = e.target;

  if (divSelectArea.style.display == "block" && clic != divSelectArea) {
    divSelectArea.style.display = "none";
  }

}, false);



function SelectArea(element){
  var prg = document.getElementById(element).innerHTML; 
  var inputNombre = document.getElementById("selectArea");
  inputNombre.value = prg;
}
