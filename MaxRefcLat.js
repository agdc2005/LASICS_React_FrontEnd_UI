// PlanStartDateDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";

export const MaxRefcLatVal = ({ maxrefclat,refclatval,onMaxRefcLatChange }) => {

  const handleMaxRefcLatChange = (e) => {
    console.log(e.target.value);
    onMaxRefcLatChange(e.target.value);
  };

  return ( 
  <div>
     <label for="maxrefclat">Set Max. Center Lat. Target 1: </label>
     <input type="text" value={maxrefclat} onChange={handleMaxRefcLatChange} />
  </div>
  )
}
