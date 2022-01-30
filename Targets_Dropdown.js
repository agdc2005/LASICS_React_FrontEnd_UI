// Dropdown.js 

import React from "react";
import {
  DropdownWrapper,
  StyledSelect,
  StyledOption,
  StyledLabel,
  StyledButton,
} from "../styles.js";

export function Dropdown(props) {
  return (
    <DropdownWrapper
      action={props.action}
      onChange={props.onChange}
    >
      <StyledLabel htmlFor="targets">
        {props.formLabel}
      </StyledLabel>
      <StyledSelect id="targets" name="targets">
        {props.children}
      </StyledSelect>
      <StyledButton type="Select Reference" value={props.buttonText} />
    </DropdownWrapper>
  );
}

export function Option(props) {
  return (
    <StyledOption selected={props.selected}>
      {props.value}
    </StyledOption>
  );
}


-----ORIGINAL

import React from 'react';

class Targets_dropdownlist extends React.component
{
    render() {
        //return <div className="drop-down">
                 //<p>Render a target dropdown here from the values object</p>
                    //<select>{
                     //this.state.values.map((obj) => {
                     //return <option value={obj.id}>{obj.name}</option>
                    //})
                    //}</select>
               //</div>;

        return <div className="drop-down">
              {['targetName'].map(key => (
                 <select key={key}>
                    {this.state.data.map(({ [key]: value }) => <option key={value}>{value}</option>)}
                 </select>
              ))}
               </div>;
    //<div>
        //<select>
            //<option> --Select Reference-- </option> 
            //<option><\option>
        //</select>
    //</div>
    }
}

export Targets_dropdownlist;
