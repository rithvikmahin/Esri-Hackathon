import Globe from "./Globe.png";
import Search from "./Search";
import { Image } from "react-bootstrap";
import "./Home.css";
import { React, useState } from "react";
import axios from "axios";

export function Home() {

    const [input, setInput] = useState("");
    
    const updateInput  = (input) => {
        if (input.includes("open.spotify.com/playlist/")) {
            handleQuery(input);
        }
        setInput(input);
    }

    const handleQuery = (query) => {
        let myParams = {
            data: query
        }

        axios.post('http://127.0.0.1:5000/api', myParams).then((response) => {
            console.log(response);
        }).catch((error) => {
            console.log(error);
        });
    }

    return (
        <div>
            <div className="rowA">
                <Image width={250} src={Globe} style={{ paddingRight: "2%" }}></Image>
                <div className="GeoTune" style={{ fontSize: "500%" }}>
                    GeoTune
                </div>
            </div>
            <div className="rowB" style={{ fontSize: "200%" }}>
                Where is your music from? Put your playlist to the test:
            </div>
            <div className="rowA">
                <Search input={input} onChange={updateInput}></Search>
            </div>
        </div>
    );  
}


