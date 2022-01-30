// TargetDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";
import {
  DropdownWrapper,
  StyledSelect,
  StyledOption,
  StyledLabel,
  StyledButton,
} from "../styles.js";

export function TargetDropdown(props) {
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
      <StyledButton type="Select Target" value={props.buttonText} />
    </DropdownWrapper>
  );
}

export function TarOption(props) {
  return (
    <StyledOption selected={props.selected}>
      {props.value}
    </StyledOption>
  );
}
