import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import '../styles/main.css';
import '../styles/pygments.css';
import { render } from 'react-dom';
import React from 'react';

//// import 1
// import { App } from './app.jsx';
// this version requires in jsx:
// class App extends React.Component {...
// module.exports = { App };

//// import 2
import App from './app.jsx';
// this version requires in jsx:
// export default class App extends React.Component {...

render(
  <App />,
  document.getElementById('main')
);

var mod = require('./mod.js');
// // now use all the exports from mod

console.log(mod());
