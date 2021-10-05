import React, {Component} from "react";



class Jokes extends Component{
    state= {joke: {}};

    componentDidMount() {
        console.log ('jokes mounted')
        fetch ("http://www.boredapi.com/api/activity/")
            .then (response=>response.json())
                .then(json=>this.setState({joke:json}));

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

