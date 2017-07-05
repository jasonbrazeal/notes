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

//// import 2
// import App from './app.jsx'; - in main.js
export default class App extends React.Component {
   render() {
      return (
         <h1>Hello, World from app.jsx!</h1>
      );
   }
}
