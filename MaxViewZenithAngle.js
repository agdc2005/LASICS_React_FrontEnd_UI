// MaxViewZenithAngle.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";

//https://reactjs.org/docs/lists-and-keys.html
//Keys help React identify which items have changed, are added, or are removed. 
//Keys should be given to the elements inside the array to give the elements a stable identity:

export const MaxViewZenithAngle = ({ maxvza,vzaval,onVZAChange }) => {

  const handleVZAChange = (e) => {
    console.log(e.target.value);
    onVZAChange(e.target.value);
  };

  return ( 
  <div>
     <label for="maxvza">Set Max. VZA: </label>
     <select name="maxvza" id="maxvza" onChange={handleVZAChange}>
       {maxvza.map(s => <option key={s.toString()} value = {s}>{s}</option>)}
     </select>
  </div>
  )
}
