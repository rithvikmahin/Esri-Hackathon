import React from 'react';
import * as ReactDOM from 'react-dom';
import { Map } from '@esri/react-arcgis';
import { loadCss } from 'esri-loader';

const apiKey = "AAPK1fa9fc0fed594e7db7b95c5846839e55lg5ylhrBg3N82Yn-bkHg2FIsabtiQ5Xdie2jbwEuNcUWHcrz0rWijSZdrtIr-iJY";

class MusicMap extends React.Component {
    constructor() {
        super();
        loadCss();
    }

    componentDidMount() {

        

        /*esriConfig.apiKey = apiKey;

        const map = new Map({
            basemap: "dark-gray" // Basemap layer service
        });
        
        const view = new MapView({
            map: map,
            center: [-118.805, 34.027], // Longitude, latitude
            zoom: 13, // Zoom level
            container: "viewDiv" // Div element
        });*/
    }

    componentWillUnmount() {

    }

    render() {
        return null; //<Map />;
    }
}

export default MusicMap;