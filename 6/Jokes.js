import React, {Component} from "react";


class Jokes extends Component {
    constructor(props) {
        super(props)
        /*
       let activity = {
            activity:"running",
           type:"sport"

       }

         */
        this.state = {jokes:[]} ;
        this.foo2 = this.foo2.bind(this)
        this.showJokes= this.showJokes.bind(this)

        console.log("1")
    }

showJokes(){
    //this.state.jokes=[]
    this.setState({jokes:[]})
    for (let i=0; i<5; i++) {
        fetch("http://www.boredapi.com/api/activity/")
            .then(response => response.json())
            .then(json => this.foo2(json))
        }

    }


    foo2(json) {


        let _jokes=this.state.jokes

        _jokes.push(json.activity)
        console.log(_jokes)


        this.setState({jokes:_jokes})

       console.log(this.state.jokes.length)
        console.log(this.state.jokes)
        }


    render()
    {

      // this actually works, but turned out to be unnecessary
    //let _jokes=this.state.jokes
        console.log("jokes type", typeof this.state.jokes)
        return (

        <div>
<p>
            {this.state.jokes.length}

</p>


        <div>

                {
                    this.state.jokes.map(joke=> {
                        return (<p>{joke}</p>)
                    }
                                )
                }

        </div>
                            <button onClick={this.showJokes}>
                                Read more
                            </button>


                        </div>



                    )
                }

}





export default Jokes;

