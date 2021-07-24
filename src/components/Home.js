import Globe from "./Globe.png";
import Search from "./Search";
import { Image } from "react-bootstrap";
import "./Home.css";
import { React, useState } from "react";

export function Home() {

    const [input, setInput] = useState("");
    
    const updateInput  = (input) => {
        setInput(input);
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


