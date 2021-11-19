document.getElementById("imgArticulo").onchange = function(e) {
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


function mostrarError(element,mensaje){
  document.getElementById(element).innerHTML=mensaje;
}


function btnGuardarArticulo(){
  var errores=false;

  var inputNombre = document.getElementById("nombreArticulo").value;
  if(inputNombre.length==0){
    mostrarError('msErrorNombre','Ingresa un nombre.');
    errores=true;
  }else{
    mostrarError('msErrorNombre','');
    errores=false;
  }

  var inputMarca = document.getElementById("marcaArticulo").value;
  if(inputMarca.length==0){
    mostrarError('msErrorMarca','Ingresa una marca.');
    errores=true;
  }else{
    mostrarError('msErrorMarca','');
    errores=false;
  }

  var inputModelo = document.getElementById("modeloArticulo").value;
  if(inputModelo.length==0){
    mostrarError('msErrorModelo','Ingresa un modelo.');
    errores=true;
  }else{
    mostrarError('msErrorModelo','');
    errores=false;
  }

  var inputArea = document.getElementById("selectArea").value;
  if(inputArea.length==0){
    mostrarError('msErrorArea','Ingresa una area.');
    errores=true;
  }else{
    mostrarError('msErrorArea','');
    errores=false;
  }


  var inputCantidad = document.getElementById("cantidadArticulo").value;
  if(inputCantidad.length==0){
    mostrarError('msErrorCantidad','Ingresa una cantidad.');
    errores=true;
  }else{
    mostrarError('msErrorCantidad','');
    errores=false;
  }

  var inputImg = document.getElementById("imgArticulo").value;
  if(inputImg==''){
    mostrarError('msErrorImg','Ingresa una imagen.');
    errores=true;
  }else{
    mostrarError('msErrorImg','');
    errores=false;
  }

  if(!errores){
    alert("listo para subir");
  }

}

