import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import App from './components/App'
import './index.css'

//ReactDOM.render(<App/>, document.getElementById("root"));

new Promise (resolve =>{
setTimeout(()=>{
 resolve('bears, beeets galastica');

    }, 5000);

})
    .then (quote=>{console.log(quote)})

console.log("oh my god, this will go first")


const z = {name:"John", age:30, "car":null};

let zz= []
zz.push (z)

console.log(z)
console.log(zz)

