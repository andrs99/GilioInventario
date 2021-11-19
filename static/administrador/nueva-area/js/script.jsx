var state ={
    data: [{
        "id": 1,
        "title": "San Miguel de Allende",
        "contenido": "Dentro de San Miguel de Allende, en Guanajuato, hallamos bonitas zonas verdes que dotan a la ciudad de un encanto único y un paisaje urbano que merece la pena detenerse a admirar..",
        "img": "https://astelus.com/wp-content/viajes/los-bonitos-jardines-de-san-miguel-de-allende-mexico.jpg"
    },{
        "id": 2,
        "title": "Cappadocia",
        "contenido": "la Cappadocia es subiéndonos a un globo aerostático. Las vistas son una verdadera fantasía. La naturaleza ha moldeado a su antojo valles enteros de depresiones y barrancos.",
        "img": "https://aws.traveler.es/prod/designs/v1/assets/1000x667/21252.jpg"
    },{
        "id": 3,
        "title": "Ik Kil",
        "contenido": "En México hallamos varios exóticos cenotes en los que los viajeros acostumbran a bañarse. Estos hundimientos, también conocidos como torcas, tienen un origen kárstico.",
        "img": "https://astelus.com/wp-content/viajes/cenote-ik-kil-yucatan-mexico.jpg"
        
    },{
        "id": 4,
        "title": "Montañas Odle",
        "contenido": "las montañas Odle, en Italia, forman uno de los parajes más desafiantes que podemos encontrar en las Dolomitas.",
        "img": "https://aws.traveler.es/prod/designs/v1/assets/1000x667/21251.jpg"
    }]
}

function msError(mensaje,elemento){
    const element = <label>Ingrese el nombre</label>
    ReactDOM.render(element, document.getElementById(elemento));
}