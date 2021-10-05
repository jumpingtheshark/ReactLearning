import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import App from './App'
import './index.css'

ReactDOM.render(<App/>, document.getElementById("root"));




class ComponentClass extends Component {


}
class RegularClass {


}





const regularClassInstance = new RegularClass();
const componentClassInstance = new ComponentClass();


console.log ('regular', regularClassInstance)
console.log ('component', componentClassInstance)

class Animal {

        constructor(name, age) {
        this.name=name
        this.age=age;


    }


    speak() {
        console.log('I am ', this.age, 'years old');
    }

}

const animal1= new Animal('Simba', 3);
animal1.speak();
console.log(animal1)



class Lion extends Animal {
    constructor(name, age, speed) {
        super(name, age);
    }


    roar() {

        console.log(
            'ROAAAR! I have ',
            this.furColor,
            'fur, and I can run',
            this.speed,
            'miles an hour'
        );

    }

}

const lion1= new Lion('mufasa', 20, 'golden', 25)
lion1.roar()
console.log(lion1)
