import React  from 'react';

//https://reactjs.org/docs/lists-and-keys.html
//Keys help React identify which items have changed, are added, or are removed. 
//Keys should be given to the elements inside the array to give the elements a stable identity:

export const DaysInPlan = ({ daysinplan, dipval, onDIPChange }) => {

  const handleDIPChange = (e) => {
    console.log(e.target.value);
    onDIPChange(e.target.value);
  };


  //const inc = () => { setDaysinPlan(countdaysinplan+1); };
  //const dec = () => { setDaysinPlan(countdaysinplan-1); };

  return (
  <div>
     <label for="daysinplan">Choose Number of Days in Plan: </label>
     <select name="daysinplan" id="daysinplan" onChange={handleDIPChange}>
       {daysinplan.map(s => <option key={s.toString()} value = {s}>{s}</option>)}
     </select>
  </div>
  )
}
