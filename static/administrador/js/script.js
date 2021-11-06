// const element = <h1>Hello, world</h1>;
// ReactDOM.render(element, document.getElementById('root'));


// function Welcome(props) {
//   return <h1>Hello, {props.name}</h1>;
// }

// function App() {
//   return (
//     <div>
//       <Welcome name="Sara" />
//       <Welcome name="Cahal" />
//       <Welcome name="Edite" />
//     </div>
//   );
// }

// ReactDOM.render(
//   <App />,
//   document.getElementById('root')
// );




// almacenando el div y el boton en unas variables
var div = document.getElementById('despliegue');
var but = document.getElementById('boton');

//la funcion que oculta y muestra
function showHide(e) {
  e.preventDefault();

  if (div.style.display == "none") {
    div.style.display = "block";
  } else if (div.style.display == "block") {
    div.style.display = "none";

  }
  e.stopPropagation();
}
//al hacer click en el boton
but.addEventListener("click", showHide, false);

//funcion para cualquier clic en el documento
document.addEventListener("click", function (e) {

  //obtiendo informacion del DOM para  
  console.log(e.target);
  var clic = e.target;

  if (div.style.display == "block" && clic != div) {
    div.style.display = "none";
  }

}, false);



const btnLogout = document.getElementById('logout');
btnLogout.addEventListener('click', function (e) {
  window.location.href = "http://127.0.0.1:8000/logout/";
  e.stopPropagation();
});


const btnHome = document.getElementById('btnHome');
const btnInventario = document.getElementById('btnInventario');

var URLactual = window.location;

if(URLactual == 'http://127.0.0.1:8000/administrador/'){
  btnHome.classList.add("box-item-panel-active");
}else if (URLactual == 'http://127.0.0.1:8000/administrador/inventario'){
  btnInventario.classList.add("box-item-panel-active");
}

btnHome.addEventListener('click', function (e) {
  window.location.href = "http://127.0.0.1:8000/administrador/";
});
btnInventario.addEventListener('click', function (e) {
  window.location.href = "http://127.0.0.1:8000/administrador/inventario";
});


