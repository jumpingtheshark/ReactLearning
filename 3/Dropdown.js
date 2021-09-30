import React, { Component } from 'react';
import PROJECTS from '../data/project'
import Table from "./Table";


class Dropdown extends Component {
    state = {selectedID:1}

    onClick=()=> {
        //this.setState({displayBio: !this.state.displayBio})
        //alert("I just got clicked")
        let e= document.getElementById("projectsDDL").value
        //alert(e)
        this.setState({selectedID:e})// set state


    }
    getTitle(choice)  {
        let sid=this.state.selectedID //get state
        let project = PROJECTS.find(x=>x.id==sid)
        switch (choice){
            case "title":
                return project.title;
                break;

            case "description":
                return project.description
                break;

            case "link":
                return project.link
        }



    }
    render ()
    {
        console.log ('this.props', this.props)


        return (
            <div>
              Dropdown with text field example
                <p>
                    <div>
                        The guy picked:
                        {this.state.selectedID}
                        <p>Project ID: </p>
                        <p> {this.state.selectedID}</p>
                        <p> Project Title:  </p>
                        <p>
                            {this.getTitle("title")}
                        </p>
                        <p>Project Description:</p>
                        <p> {this.getTitle("description")}</p>
                        <p>Link:</p>
                        <p> {this.getTitle("link")}</p>

                    </div>

                </p>

        <p>

        <select  id="projectsDDL" >
            {
                PROJECTS.map (
                    (x) => {
                        let rval = <option value={x.id}>{x.title}</option>
                        return rval;
                        }
                    )
            }
        </select>
        </p>

                <p>

                    <button onClick = {this.onClick}>
                        click me
                    </button>

                </p>
            </div>

        )
    }

}

export default Dropdown;