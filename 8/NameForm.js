
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
        this.state =
            {
                name:'',
                philosophy: '',
                rName:'nada',
                rPhil: 'nada'
            };


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


            console.log(JSON.stringify(this.state))
            console.log('here what we are submitting')
            console.log(this.state.name)
            console.log(this.state.philosophy)
            event.preventDefault();

            //const data = {username: 'example'};
            const data = {
                name: this.state.name,
                philosophy: this.state.philosophy
            }
            console.log("about to fetch")


        let  mike = "http://localhost:5001/mike"

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
                    this.setState({rName: data.name})
                    this.setState ({rPhil: data.philosophy})
                })
                .catch((error) => {
                    console.error('Error:', error);
                });

        }






    render() {
        return (

            <div>

                <label>
                    Name:
                    <input id="name" type="text" value={this.state.name} onChange={this.handleNameChange} />

                </label>
<p></p>
                <label>
                    Philosophy:
                    <select id="philosophy" value={this.state.philosophy} onChange={this.handlePhilosophyChange} >
                   <option></option>

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

       <p></p>
            <button onClick={this.handleSubmit}> Submit</button>
                <div>
                    {this.state.rName}
                    <p></p>
                    {this.state.rPhil}
                </div>



            </div>


        );
    }
}

export default NameForm;