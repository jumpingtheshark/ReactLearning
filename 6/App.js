import React, { Component } from 'react';
import Projects from './Projects'
import SocialProfiles from "./SocialProfiles";
import profile from '../assets/profile.png'
import Title from "./Title";
import Jokes from './Jokes'

class App extends Component {
     state = {displayBio:false}
    /*
    constructor() {



        super();
    this.state = {displayBio: false };
    console.log ('Component this', this);

    this.readMore = this.readMore.bind(this)
        this.readLess = this.readLess.bind(this)
        this.toggleDisplayBio= this.toggleDisplayBio.bind(this)
    }
*/

    readMore() {
        console.log ('read more this', this);
        this.setState({displayBio:true})

    }
    readLess() {
        console.log ('read more this', this);
        this.setState({displayBio:false})

    }



    toggleDisplayBio=()=>{
        this.setState({displayBio: !this.state.displayBio})

    }


    render() {



        return (

            <div>


                <img src ={profile} alt='profile' className={'profile'}/>

                <h1>
                HI

                </h1>

                <p>
                    My Name is Mike, and I code

                    </p>
                <p>
                    I guess it's fun, idk

                </p>
                <p>
                    {this.state.displayBio ? <Title/>: null}



                </p>
                {
                    this.state.displayBio ? (
                        <div>
------------------------------------------------------------
                            <p>
                                I have 2 beautiful kids who always keep me busy

                                And the older one always has some activity, but we need to find more activites for the younger one.
                            </p>
                                <p>
                                At work I listen to podcasts to get through the day.
                            </p>
                            <p>
                                <Jokes></Jokes>
                            </p>
                            <div>
                                <button onClick = {this.toggleDisplayBio}>
                                    Show less
                                </button>
                            </div>

                        </div>
                    ):<div>
                        <button onClick={this.toggleDisplayBio}>
                            Read more
                        </button>

                    </div>

                }
<hr/>




                <hr>
                </hr>
                <Projects></Projects>
                <SocialProfiles></SocialProfiles>


            </div>
        )

    }
}

export default App;

