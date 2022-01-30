// PlanStartDateDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";
import {
  DropdownWrapper,
  StyledSelect,
  StyledOption,
  StyledLabel,
  StyledButton,
} from "../styles.js";

export function PlanStartDateDropdown(props) {
  return (
    <DropdownWrapper
      action={props.action}
      onChange={props.onChange}
    >
      <StyledLabel htmlFor="startdate">
        {props.formLabel}
      </StyledLabel>
      <StyledSelect id="startdate" name="startdate">
        {props.children}
      </StyledSelect>
      <StyledButton type="Plan Start Date" value={props.buttonText} />
    </DropdownWrapper>
  );
}
