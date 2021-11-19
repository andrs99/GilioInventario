function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


function guardarArea(){
  var furmulario = new FormData(document.getElementById('formNuevaArea'))
  fetch("/administrador/guardar-area",{
      method: "POST",
      body: furmulario,
      headers:{
          "X-CSRFToken": getCookie('csrftoken'),
      }
  })

  
}



document.getElementById("imgArea").onchange = function(e) {
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

function mostrarError(element,mensaje){
  document.getElementById(element).innerHTML=mensaje;
}



function btnGuardarArticulo(){
  var erroresImg=false;
  var erroresNombre=false;

  var inputNombre = document.getElementById("nombreArea").value;
  if(inputNombre.length==0){
    mostrarError('msErrorNombre','Ingresa un nombre.');
    erroresNombre=true;
  }else{
    mostrarError('msErrorNombre','');
    erroresNombre=false;
  }


  

  var inputImg = document.getElementById("imgArea").value;
  
  if(inputImg==''){
    mostrarError('msErrorImg','Ingresa una imagen.');
    erroresImg=true;
  }else{
    mostrarError('msErrorImg','');
    erroresImg=false;
  }

  if(!erroresImg && !erroresNombre){
    guardarArea();
    window.location="./areas";
  }
  
}

