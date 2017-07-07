import React from 'react';
// //// import 1
// // import { App } from './app.jsx'; - in main.js
// class App extends React.Component {
//    render() {
//       return (
//          <h1>Hello, World from app.jsx!</h1>
//       );
//    }
// }

// module.exports = { App };

// //// import 2
// // import App from './app.jsx'; - in main.js
// export class App extends React.Component {
//    render() {
//       return (
//          <h1>Hello, World from app.jsx!</h1>
//       );
//    }
// }
//  export var test = 'test';

// export class DynamicSearch extends React.Component {

//   constructor() {
//     super();
//     // set up "this" for the handle change function
//     this.handleChange = this.handleChange.bind(this);
//     this.state = {
//       searchString: ''
//     };
//   }

//   // sets state, triggers render method
//   handleChange(event){
//     // grab value form input box
//     this.setState({searchString:event.target.value});
//     console.log("scope updated!");
//   }

//   render() {
//     var countries = this.props.items;
//     var searchString = this.state.searchString.trim().toLowerCase();

//     // filter countries list by value from input box
//     if(searchString.length > 0){
//       countries = countries.filter(function(country){
//         return country.name.toLowerCase().match(searchString);
//       });
//     }

//     return (
//       <div>
//         <input type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="Search!" />
//         <ul>
//           { countries.map(function(country, i){
//             return <li key={i}>{country.name}</li>
//           }) }
//         </ul>
//       </div>
//     )
//   }

// };

// // list of countries, defined with JavaScript object literals
// export var countries = [
//   {"name": "Sweden"}, {"name": "China"}, {"name": "Peru"}, {"name": "Czech Republic"},
//   {"name": "Bolivia"}, {"name": "Latvia"}, {"name": "Samoa"}, {"name": "Armenia"},
//   {"name": "Greenland"}, {"name": "Cuba"}, {"name": "Western Sahara"}, {"name": "Ethiopia"},
//   {"name": "Malaysia"}, {"name": "Argentina"}, {"name": "Uganda"}, {"name": "Chile"},
//   {"name": "Aruba"}, {"name": "Japan"}, {"name": "Trinidad and Tobago"}, {"name": "Italy"},
//   {"name": "Cambodia"}, {"name": "Iceland"}, {"name": "Dominican Republic"}, {"name": "Turkey"},
//   {"name": "Spain"}, {"name": "Poland"}, {"name": "Haiti"}
// ];


export class NoteSearch extends React.Component {

  constructor() {
    super();
    // set up "this" for the handle change function
    this.handleChange = this.handleChange.bind(this);
    this.state = {
      searchString: '',
      notes: [],
      matches: []
    };
  }

  componentDidMount() {
    var notes = Object.getOwnPropertyNames(this);
    // get notes via ajax
    this.setState({
      notes: notes,
      matches: notes
    });
  }

   // componentWillUnmount() {
   // }

  // sets state, triggers render method
  handleChange(event){
    var searchString = event.target.value.trim().toLowerCase();
    // grab value from input box
    this.setState({
      searchString: searchString,
    });
    // filter countries list by value from input box
    if(searchString.length > 0){
      var matches = this.state.notes.filter(function(note){
        return note.toLowerCase().match(searchString);
      });
      this.setState({
        matches: matches
      });
    } else {
      this.setState({
        matches: this.state.notes
      });
    }
  }

  render() {
    return (
      <div>
        <input type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="Search..." />
        <ul>
          { this.state.matches.map(function(note, i){
            return <li key={i}>{note}</li>
          }) }
        </ul>
      </div>
    )
  }

};
