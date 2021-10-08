import React, {Component} from "react";
import PROJECTS from '../data/project'




class Project extends Component {
render ()
{
    console.log ('this.props', this.props)
    const {title, image, description, link}=this.props.project;

    return (
        <div style={{ display: 'inline-block', width:300, margin:10}}>
            <h3>
               stupid {title}
            </h3>
            <p>
            <img src={image } style= {{width:200, height:120}} alt='profile'/>
            </p>
            <p>
            {description}</p>
                <p >
                <a href={link}>{link}</a>
                </p>

        </div>

    )
}

}


class Projects extends Component {
    render() {

        return (

            <div>
                <h2>
                    Highlighted Projects

                    <div>
                        {
                            PROJECTS.map(
                                (PROJECT) => {
                                    return (
                                        <Project key={PROJECT.id } project = {PROJECT}></Project>
                                    )

                                })

                        }

                    </div>
                </h2>

            </div>
        )


    }

}



export default Projects;