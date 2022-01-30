import React from 'react';

//https://reactjs.org/docs/lists-and-keys.html
//Keys help React identify which items have changed, are added, or are removed. 
//Keys should be given to the elements inside the array to give the elements a stable identity:

export const Targets = ({ targets,tarval,onTarChange }) => {

  const handleTarChange = (e) => {
    console.log(e.target.value);
    onTarChange(e.target.value);
  };

  return (
  //<div>{targets.map(s => (<li>{s}</li>))}</div>
  <div>
     <label for="targets">Choose Target 2 : </label>
     <select name="targets" id="targets" onChange={handleTarChange}>
       {targets.map(s => <option key={s.toString()} value = {s}>{s}</option>)}
     </select>
  </div>
  )
}
