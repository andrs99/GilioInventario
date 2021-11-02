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
  e.stopPropagation();
  if (div.style.display == "none") {
    div.style.display = "block";
  } else if (div.style.display == "block") {
    div.style.display = "none";

  }
  e.stopPropagation()
}
//al hacer click en el boton
but.addEventListener("click", showHide, false);

//funcion para cualquier clic en el documento
document.addEventListener("click", function (e) {

  //obtiendo informacion del DOM para  
  var clic = e.target;

  if (div.style.display == "block" && clic != div) {
    div.style.display = "none";
  }
}, false);