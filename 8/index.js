import React, {Component} from 'react';
import ReactDOM from 'react-dom';
//import App from './App'


//ReactDOM.render(<App/>, document.getElementById("root"));


console.log("about to fetch")
let bored = "http://www.boredapi.com/api/activity"
let mike = "http://localhost:5001/mike"
const data = { username: 'example' };


function foo1() {
    fetch(mike)
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(response => console.log("problem!!!"))
}

function foo2() {
    fetch(mike, {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

}

function foo3 (){
    //url?a=1&b=2
    let url="http://localhost:5001/mike_get"
    fetch(url + "?"+ new URLSearchParams({
        foo: 'value',
        bar: 2,
    })).then (response=>response.json())
        .then (json=>console.log(json))



}

foo3()







