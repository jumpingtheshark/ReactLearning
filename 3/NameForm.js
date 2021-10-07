
import React, { Component } from 'react';



//<form>
//    <label>
 //       Name:
 //       <input type="text" name="name" />
  //  </label>
  //  <input type="submit" value="Submit" />
//</form>

//https://stackoverflow.com/questions/46640024/how-do-i-post-form-data-with-fetch-api

class NameForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value:''};


        //this.handleChange = this.handleChange.bind(this)
        this.handleNameChange = this.handleNameChange.bind(this)
        this.handlePhilosophyChange = this.handlePhilosophyChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleNameChange(event) {
        this.setState({name: event.target.value});
        console.log(event.target.value )

    }

    handlePhilosophyChange(event) {
        this.setState({philosophy: event.target.value});
        console.log(event.target.value )
    }

// todo, add get.post and run it inside a golang job or something.
    // and put it a get fetch on the construtor.  
    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        console.log(JSON.stringify(this.state))
        alert ('here what we are submitting')
        event.preventDefault();
    }



    render() {
        return (
            <form onSubmit={this.handleSubmit} >
                <label>
                    Name:
                    <input id="name" type="text" value={this.state.name} onChange={this.handleNameChange} />

                </label>
              <p>
                <label>
                    Philosophy:
                    <select id="philosophy" value={this.state.philosophy} onChange={this.handlePhilosophyChange} >
                    <option>
                        capitalism

                    </option>

                        <option>
                            socialism

                        </option>
                        <option>
                            marxism

                        </option>

                    </select>

                </label>
              </p>

                <p>
                <input type="submit" value="Submit" />
                </p>
                </form>
        );
    }
}

export default NameForm;