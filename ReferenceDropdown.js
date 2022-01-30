// ReferenceDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";
import {
  DropdownWrapper,
  StyledSelect,
  StyledOption,
  StyledLabel,
  StyledButton,
} from "../styles.js";

export function ReferenceDropdown(props) {
  return (
    <DropdownWrapper
      action={props.action}
      onChange={props.onChange}
    >
      <StyledLabel htmlFor="references">
        {props.formLabel}
      </StyledLabel>
      <StyledSelect id="references" name="references">
        {props.children}
      </StyledSelect>
      <StyledButton type="Select Reference" value={props.buttonText} />
    </DropdownWrapper>
  );
}

export function RefOption(props) {
  return (
    <StyledOption selected={props.selected}>
      {props.value}
    </StyledOption>
  );
}
