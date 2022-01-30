// MaxSolarZenithAngleDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";

export const MaxTimeBetnMeas = ({ maxtimebetmeas }) => {
  return ( 
  <div>
     <label for="maxtimebetnmeas">Set Max. SZA: </label>
     <select name="maxtimebetnmeas" id="maxtimebetnmeas">
       {maxtimebetnmeas.map(s => <option value = {s}>{s}</option>)}
     </select>
  </div>
  )
}
