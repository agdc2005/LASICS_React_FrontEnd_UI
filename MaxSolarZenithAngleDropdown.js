// MaxSolarZenithAngleDropdown.js 
//https://www.newline.co/@andreeamaco/react-dropdown-tutorial-for-beginners-create-a-dropdown-menu-from-scratch--9831d197

import React from "react";
import {
  DropdownWrapper,
  StyledSelect,
  StyledOption,
  StyledLabel,
  StyledButton,
} from "../styles.js";

export function MaxSolarZenithAngleDropdown(props) {
  return (
    <DropdownWrapper
      action={props.action}
      onChange={props.onChange}
    >
      <StyledLabel htmlFor="maxsza">
        {props.formLabel}
      </StyledLabel>
      <StyledSelect id="maxsza" name="maxsza">
        {props.children}
      </StyledSelect>
      <StyledButton type="Maximum Solar Zenith Angle" value={props.buttonText} />
    </DropdownWrapper>
  );
}

export function MaxSZAOption(props) {
  return (
    <StyledOption selected={props.selected}>
      {props.value}
    </StyledOption>
  );
}
