// PlanStartDateDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";

export const MinRefcLatVal = ({ minrefclat,refclatval,onMinRefcLatChange }) => {

  const handleMinRefcLatChange = (e) => {
    console.log(e.target.value);
    onMinRefcLatChange(e.target.value);
  };

  return ( 
  <div>
     <label for="minrefclat">Set Min. Center Lat. Target 1: </label>
     <input type="text" value={minrefclat} onChange={handleMinRefcLatChange} />
  </div>
  )
}
