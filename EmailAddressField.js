import React from 'react';

//https://reactjs.org/docs/lists-and-keys.html
// A “key” is a special string attribute 
//Keys help React identify which items have changed, are added, or are removed. 
//Keys should be given to the elements inside the array to give the elements a stable identity:

//Reference Video: https://www.youtube.com/watch?v=HF4o9KAZNxw
// Lifting State up from Child Component to Parent ../App1.js
export const EmailAddressField = ({emailval,onEmailChange}) => {

  const handleEmailChange = (e) => {
    console.log(e.target.value);
    onEmailChange(e.target.value);
  };

  return (
  <div>
    <label htmlFor="email">Your Email Address here</label> <br />
      <input  type="email" name="email" onChange={handleEmailChange}/> <br />
  </div>
  )
}
