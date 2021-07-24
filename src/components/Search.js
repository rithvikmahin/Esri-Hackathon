import React from 'react';

const Search = (props) => {
  const BarStyling = { width:"20rem", padding:"0.5rem", border: "none", borderRadius: "25px", outline: "none" };
  return (
    <input 
     style={BarStyling}
     key="Test"
     value={props.input}
     placeholder={"Insert Spotify playlist link"}
     onChange={(e) => props.onChange(e.target.value)}
    />
  );
}

export default Search