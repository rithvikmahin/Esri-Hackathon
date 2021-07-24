import Globe from "./Globe.png";
import "./Home.css";

export function Home() {
    return (
        <div>
            <div className="Image-Container">
                <img width={100} style={{ alignSelf: 'center' }} src={Globe}></img>
            </div>
        </div>
    );  
}


