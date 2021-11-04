import React, {Component} from "react";
// npm start

class Tracks extends Component {
    constructor() {
        super();


        this.state ={spotifyID: '',
            tracks:[],
            tracksJson:{}
        }


        //  this.state.genres=[]
        // this.setState({genres:this.props.genres})


    }

    componentDidMount(){
        this.setState({spotifyID:this.props.spotifyID})
        let spotifyID = this.props.spotifyID

       // console.log ("top tracks query",  spotifyID)


        let TRACKS_URL =  "http://127.0.0.1:5001/tracks?spotify_id="+spotifyID
       // console.log(TRACKS_URL)
        fetch (TRACKS_URL)
            .then (response=>response.json())
            .then (json=>this.foo2(json))


    }

    foo2(j) {

        //console.log(j)


        //const {blah, tracks}=j
        let tracks = j["top_tracks"]
        let _tracks =[]

        this.setState({tracks:tracks})
        console.log(tracks)


    }

    render() {

        return (
            <div>
                Top Tracks
                <p>
                {this.state.spotifyID}
                </p>
                <p>
                    {this.state.tracks.map(
                        (track)=>{
                            return (
                           <p>
                            <a href={track["preview_url"]}
                               target= {"_blank"}
                            >
                                { track["name"]}
                            </a>
                           </p>
                               )
                        }

                    )}

                </p>
                </div>

        )

    }


}

export default Tracks;
