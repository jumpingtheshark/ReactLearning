import React, { Component } from 'react';

class App extends Component {

    constructor() {
        super();
    this.state = {displayBio: true };

    }


    render() {



        return (

            <div>

                <h1>
                HI

                </h1>

                <p>
                    My Name is Mike, and I code

                    </p>
                <p>
                    I guess it's fun, idk

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

                        </div>
                    ):null

                }


            </div>
        )

    }
}

export default App;

