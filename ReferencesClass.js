import React, { Component } from 'react';

class ReferencesClass extends React.Component {
 constructor(props) {
    super(props)
    references = {references}
    this.state = { refvalue: "NOAA 20" };
    this.handleRefSelect = this.handleRefSelect.bind(this);
    this.handleRefSubmit = this.handleRefSubmit.bind(this);
  }

  handleRefSelect(event) {
    this.setState({ refvalue: event.target.refvalue });
  }

  handleRefSubmit(event) {
    event.preventDefault();
    console.log(this.state.refvalue);
  }

  render() {
     return (
     <div>
        <label for="references">Choose a Reference: </label>
        <select name="references" id="references">
          {references.map(s => <option value = {s}>{s}</option>)}
       </select>
     </div>
    )
  }

}

export default ReferencesClass;
