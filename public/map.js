// module references
let config;
let esriMap;
let esriMapView;
let esriGraphic;
let esriGraphicsLayer;
let esriFeatureLayer;

// created objects
let map;
let view;
let graphicsLayer;

// dummy dataset - just a placeholder rn
let dataset = { "Taylor Swift": "US" };

require([
    // modules
    "esri/config",
    "esri/Map",
    "esri/views/MapView",
    "esri/Graphic",
    "esri/layers/GraphicsLayer",
    "esri/layers/FeatureLayer"
    ], function(esriConfig, Map, MapView, Graphic, GraphicsLayer, FeatureLayer) {
        
    // set module references
    config = esriConfig;
    esriMap = Map;
    esriMapView = MapView;
    esriGraphic = Graphic;
    esriGraphicsLayer = GraphicsLayer;
    esriFeatureLayer = FeatureLayer;

    // create map
    initMap();

    addCountries();
});

// init basic map
function initMap() {
    config.apiKey = "AAPK1fa9fc0fed594e7db7b95c5846839e55lg5ylhrBg3N82Yn-bkHg2FIsabtiQ5Xdie2jbwEuNcUWHcrz0rWijSZdrtIr-iJY";

    // map object - change basemap to change appearance
    map = new esriMap({
        basemap: "dark-gray" //Basemap layer service
    });

    // map view object - change starting location and zoom
    view = new esriMapView({
        map: map,
        center: [0, 35], // Longitude, latitude
        zoom: 3,
        container: "viewDiv"
    });
  
    // add graphics layer to display points
    graphicsLayer = new esriGraphicsLayer();
    map.add(graphicsLayer);
}

// shade in a country on the map
function addCountries() {
    const countryStyles = [];
    const popups = [];
    for (key in dataset) {
        countryStyles.push(createStyle(dataset[key], "#1db954"))
        popups.push(generatePopup(dataset[key], key));
    }

    // renderer; filters data to return by ISO code
    const countriesRenderer = {
        type: "unique-value",
        field: "ISO_CC",
        uniqueValueInfos: countryStyles
    };

    // feature layer containing country data (polygons)
    const countriesLayer = new esriFeatureLayer({
        url: "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/World_Countries/FeatureServer/0",
        renderer: countriesRenderer,
        opacity: 0.8,
        popupTemplate: popups[0]
    });

    map.add(countriesLayer);
}

function generatePopup(country, artist) {
    return {
        "title": country,
        "content": `<b>Artists: </b> ${artist}<br>`
    }
}

// function that determines visual style
function createStyle(value, color) {
    return {
        "value": value,
        "symbol": {
            "color": color,
            "type": "simple-fill",
            "style": "solid",
            "outline": {
                color: color,
                width: "1px"
            }
        },
        "label": value
    };
}