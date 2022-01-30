import React  from 'react';

//https://reactjs.org/docs/lists-and-keys.html
//Keys help React identify which items have changed, are added, or are removed. 
//Keys should be given to the elements inside the array to give the elements a stable identity:

export const MaxTimeDiffBetnRefandTar = ({ maxtimediff, timediffbetnrefandtarval, onTimeDiffChange }) => {

  const handleTimeDiffChange = (e) => {
    console.log(e.target.value);
    onTimeDiffChange(e.target.value);
  };

  return (
  <div>
     <label for="maxtimediff">Choose Max. Time Difference between Reference and Target (Minutes): </label>
     <select name="maxtimediff" id="maxtimediff" onChange={handleTimeDiffChange}>
       {maxtimediff.map(s => <option key={s.toString()} value = {s}>{s}</option>)}
     </select>
  </div>
  )
}
