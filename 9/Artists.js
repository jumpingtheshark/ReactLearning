import './App.css';
import React, {Component} from "react";
// npm start

class Artist extends Component {
    constructor() {
        super();
      //  this.state.genres=[]
       // this.setState({genres:this.props.genres})


    }

        render() {

            //{"image_url":"","name":"","spotify_id":"","total_followers":56146, genres}
            return (
                <div>

                    <p>
                        <a href={"https://open.spotify.com/artist/" + this.props.spotifyID}>
                            {this.props.name}

                        </a>
                    </p>
                    <p style={{}}>
                        <ul>
                            {this.props.genres.map(genre=>{return <li> {genre} </li>})}
                        </ul>
                    </p>

                    <p>
                        {this.props.followers}
                    </p>

                    <img src={this.props.imageUrl}
                         style= {{
                             width:400,
                             height:400,
                             borderRadius:400
                         }}
                    >
                    </img>

                </div>

            )

        }


    }

export default Artist;
