function validar(){
    var usuario = document.getElementById('usuario').value
    var password = document.getElementById('password').value
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    xhr.addEventListener("readystatechange", function() {
    if(this.readyState === 4) {
        // console.log(this.status);
        obj=JSON.parse(this.responseText)
        console.log(obj);
        if(obj['return']==1){
            window.location="./login_validar/";
        }else if(obj['return']==0){
            error("Usuario o contraseña incorrectos.");
            document.getElementById("usuario").value = "";
            document.getElementById("password").value = "";
            elemnt = document.getElementById("imput-usuario");
            elemnt.style.boxShadow = '0px 0px 0px 2px rgba(255, 0, 0, 0.781) inset';
            elemnt = document.getElementById("imput-password");
            elemnt.style.boxShadow = '0px 0px 0px 2px rgba(255, 0, 0, 0.781) inset';
            document.getElementById("usuario").focus();
        }
    }
    });
    xhr.open("GET","http://127.0.0.1:8000/login_ajax?usuario="+usuario+"&password="+password);
    xhr.send();
}

function ingresar(){
    var furmulario = new FormData(document.getElementById('formulario'))
    var usuario = furmulario.get('usuario');
    var password = furmulario.get('password');

    var errores = false;

    

    elemnt = document.getElementById("div-error");
    elemnt.style.visibility = 'hidden';
    document.getElementById('div-error').innerHTML = '';

    elemnt = document.getElementById("imput-usuario");
    elemnt.style.boxShadow = 'none';
    elemnt = document.getElementById("imput-password");
    elemnt.style.boxShadow = 'none';

    if(password.length==0){
        error("Ingrese por favor una contraseña");
        errores =  true;
        elemnt = document.getElementById("imput-password");
        elemnt.style.boxShadow = '0px 0px 0px 2px rgba(255, 0, 0, 0.781) inset';
        document.getElementById("password").focus();
    }
    else if(password.length<2){
        error("Ingrese una contraseña valida.");
        errores =  true;
        document.getElementById("password").value = "";
        elemnt = document.getElementById("imput-password");
        elemnt.style.boxShadow = '0px 0px 0px 2px rgba(255, 0, 0, 0.781) inset';
        document.getElementById("password").focus();
    }

    if(usuario.length==0){
        error("Ingrese por favor un usuario");
        errores =  true;

        elemnt = document.getElementById("imput-usuario");
        elemnt.style.boxShadow = '0px 0px 0px 2px rgba(255, 0, 0, 0.781) inset';

        document.getElementById("usuario").focus();
    }
    else if(usuario.length<10){
        error("Ingrese un usuario valido");
        errores =  true;
        document.getElementById("usuario").value = "";
        elemnt = document.getElementById("imput-usuario");
        elemnt.style.boxShadow = '0px 0px 0px 2px rgba(255, 0, 0, 0.781) inset';
        document.getElementById("password").focus();
    }else if(!usuario.includes('@')){
        error("Ingrese un usuario valido");
        errores =  true;
        document.getElementById("usuario").value = "";
        elemnt = document.getElementById("imput-usuario");
        elemnt.style.boxShadow = '0px 0px 0px 2px rgba(255, 0, 0, 0.781) inset';
        document.getElementById("password").focus();
    }
    if(!errores){
        validar();
    }
}

function error(mensaje) {
    elemnt = document.getElementById("div-error");
    elemnt.style.visibility = 'visible';
    
    element = document.createElement("div");
    element.classList.add('box-texto');
    element.innerHTML = mensaje
    contenedor = document.getElementById("div-error");
    contenedor.appendChild(element)
}
