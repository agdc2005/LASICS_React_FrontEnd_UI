// MaxDurationDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";
import {
  DropdownWrapper,
  StyledSelect,
  StyledOption,
  StyledLabel,
  StyledButton,
} from "../styles.js";

export function MaxDurationDropdown(props) {
  return (
    <DropdownWrapper
      action={props.action}
      onChange={props.onChange}
    >
      <StyledLabel htmlFor="daysinplan">
        {props.formLabel}
      </StyledLabel>
      <StyledSelect id="daysinplan" name="daysinplan">
        {props.children}
      </StyledSelect>
      <StyledButton type="Number of Days in Plan" value={props.buttonText} />
    </DropdownWrapper>
  );
}

export function MaxDurOption(props) {
  return (
    <StyledOption selected={props.selected}>
      {props.value}
    </StyledOption>
  );
}
