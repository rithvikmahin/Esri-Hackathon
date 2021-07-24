let map;
let view;
let graphicsLayer;

require([
    "esri/config",
    "esri/Map",
    "esri/views/MapView",
    "esri/Graphic",
    "esri/layers/GraphicsLayer",
    "dojo/domReady!"
], function(esriConfig, Map, MapView, Graphic, GraphicsLayer) {
    initMap(esriConfig, Map, MapView, Graphic, GraphicsLayer);
});

function initMap(esriConfig, Map, MapView, Graphic, GraphicsLayer) {

    esriConfig.apiKey = "AAPK1fa9fc0fed594e7db7b95c5846839e55lg5ylhrBg3N82Yn-bkHg2FIsabtiQ5Xdie2jbwEuNcUWHcrz0rWijSZdrtIr-iJY";

    map = new Map({
        basemap: "dark-gray"
    });

    view = new MapView({
        container: "viewDiv",
        map: map,
        zoom: 4,
        center: [15, 65] // longitude, latitude
    });

    graphicsLayer = new GraphicsLayer();
    map.add(graphicsLayer);
}

/*function addPoint() {
    const point = { //Create a point
        type: "point",
        longitude: -118.80657463861,
        latitude: 34.0005930608889
     };

     const simpleMarkerSymbol = {
        type: "simple-marker",
        color: [226, 119, 40],  // Orange
        outline: {
            color: [255, 255, 255], // White
            width: 1
        }
     };
}*/