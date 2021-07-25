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

// datasets
const dataset = JSON.parse(sessionStorage.getItem("data"))["data"];
const playlistData = dataset["ArtistsInPlaylist"];
const recData = dataset["RecommendArtists"]

// custom actions
let loadArtistsAction = {
    title: "Load Artists",
    id: "load-artists",
};

// theme colors
const playlistColor = "rgb(29, 185, 84)";
const playlistColorTrans = "rgba(29, 185, 84, 0.6)";
const recColor = "rgb(220, 20, 140)";
const recColorTrans = "rgba(220, 20, 140, 0.6)";

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

    localStorage.clear();

    // create map
    initMap();

    // add playlist data
    const playlistCountries = [];
    for (key in playlistData) {
        playlistCountries.push(playlistData[key]["country/area"]);
    }

    addCountries(playlistCountries, playlistColorTrans, playlistColor);

    // add recommendations
    const recCountries = [];
    for (key in recData) {
        recCountries.push(recData[key]);
    }

    addCountries(recCountries, recColorTrans, recColor);
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

    // Event handler that fires each time an action is clicked.
    view.popup.on("trigger-action", function(event) {
        if (event.action.id === "load-artists") {
            addArtistData();
        }
    });
  
    // add graphics layer to display points
    graphicsLayer = new esriGraphicsLayer();
    map.add(graphicsLayer);
}

// shade in a country on the map
function addCountries(countries, color, outline) {
    const countryStyles = [];
    for (country of countries) {
        countryStyles.push(createStyle(country, color, outline))
    }

    // renderer; filters data to return by ISO code
    const countriesRenderer = {
        type: "unique-value",
        field: "ISO_CC",
        uniqueValueInfos: countryStyles
    };

    const popup = generatePopup();

    // feature layer containing country data (polygons)
    const countriesLayer = new esriFeatureLayer({
        url: "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/World_Countries/FeatureServer/0",
        renderer: countriesRenderer,
        opacity: 0.8,
        outFields: ["COUNTRY", "ISO_CC"],
        popupTemplate: popup
    });

    map.add(countriesLayer);
}

// function that determines visual style
function createStyle(value, color, outline) {
    return {
        "value": value,
        "symbol": {
            "color": color,
            "type": "simple-fill",
            "style": "solid",
            "outline": {
                color: outline,
                width: "1px"
            }
        },
        "label": value
    };
}

// create the popup template
function generatePopup() {
    return {
        "title": "{COUNTRY}",
        "content": "Click Button to Load {ISO_CC} Artists...",
        actions: [ loadArtistsAction ]
    }
}

// inject the artist data into the popup
function addArtistData() {
    const artists = [];
    const countryCode = view.popup.selectedFeature.attributes["ISO_CC"];

    for (key in playlistData) {
        if (playlistData[key]["country/area"] === countryCode)
            artists.push(key);
    }
    for (key in recData) {
        if (recData[key] === countryCode)
            artists.push(key);
    }

    view.popup.content = "Artists: ";

    for (let i = 0; i < artists.length; i++) {
        view.popup.content += artists[i];
        if (i !== artists.length - 1)
            view.popup.content += ", ";
    }
}

// make side panel

// style labels
// points for cities