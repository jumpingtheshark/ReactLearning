import React, { Component } from 'react';
import PROJECTS from '../data/project'


class TableRow extends Component {
    render ()
    {
        console.log ('this.props', this.props)
        const {title,  description, link}=this.props.x;

        return (

        <tr>
            <td>
                {title}
            </td>

            <td>
                {description}
            </td>


            <td>
                {link}
            </td>

        </tr>

        )
    }

}



class Table extends Component {
    render ()
    {
       return (

           <table>
               <tr>
                   <td>title</td>
                    <td>description</td>
                   <td>link</td>
               </tr>

               {
                    PROJECTS.map(
                        (x)=>{
                            return(
                                <TableRow key = {x.id} x={x}></TableRow>
                            )
                        }

                   )
               }
       </table>
       )

    }
    }

export default Table;
