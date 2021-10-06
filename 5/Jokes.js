import React, {Component} from "react";



class Jokes extends Component {
    constructor(props) {
        super(props)
        this.state = {joke: {}};
        this.foo2 = this.foo2.bind(this)
    }





    //state= {joke: {}};

    componentDidMount() {
        console.log('jokes mounted')

/*
        fetch ("http://www.boredapi.com/api/activity/")
           .then (response=>response.json())
             .then(json=>this.setState({joke:json}))
*/

        // this was really tricky as hell.. so.. step 1..
        // the first then converts the promise to a json
        // and then the json does the rest
        fetch ("http://www.boredapi.com/api/activity/")
            .then (response=>response.json())
            .then(json=>this.foo2(json))



        /*
            let response=fetch("http://www.boredapi.com/api/activity/")
               .then (function (response) {
                    return response.json()

               })
                .then (json=>(alert (json)))
        */

}

    foo2(json) {

        this.setState({joke:json});
        const {activity, type}=json;
        alert (activity)
        alert (type)

        //for (var key in json){
          //  alert (json[key][1])
        }






    render(){
        const {activity, type}=this.state.joke;

        return (
            <div>
                <p>Activity: {activity}</p>
                <p>Type: {type}</p>
            </div>

        )

    }


}

export default Jokes;

