import React from 'react';

//https://reactjs.org/docs/lists-and-keys.html
// A “key” is a special string attribute 
//Keys help React identify which items have changed, are added, or are removed. 
//Keys should be given to the elements inside the array to give the elements a stable identity:

//Reference Video: https://www.youtube.com/watch?v=HF4o9KAZNxw
// Lifting State up from Child Component to Parent ../App1.js
export const References = ({references,refval,onRefChange}) => {

  const handleRefChange = (e) => {
    console.log(e.target.value);
    onRefChange(e.target.value);
  };

  return (
  //<div>{targets.map(s => (<li>{s}</li>))}</div>
  <div>
     <label for="references">Choose Target 1 : </label>
     <select name="references" id="references"  onChange={handleRefChange} value={refval}>
       {references.map((s) => <option key={s.toString()} value = {s}>{s}</option>)}
     </select>
  </div>
  )
}
