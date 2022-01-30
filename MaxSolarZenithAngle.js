// MaxSolarZenithAngle.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";

//https://reactjs.org/docs/lists-and-keys.html
//Keys help React identify which items have changed, are added, or are removed. 
//Keys should be given to the elements inside the array to give the elements a stable identity:

export const MaxSolarZenithAngle = ({ maxsza,szaval,onSZAChange }) => {

  const handleSZAChange = (e) => {
    console.log(e.target.value);
    onSZAChange(e.target.value);
  };

  return ( 
  <div>
     <label for="maxsza">Set Max. SZA: </label>
     <select name="maxsza" id="maxsza" onChange={handleSZAChange}>
       {maxsza.map(s => <option key={s.toString()} value = {s}>{s}</option>)}
     </select>
  </div>
  )
}
