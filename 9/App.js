import './App.css';
import React, {Component} from "react";
import Artist from './Artists'
// npm start



class App extends Component {
    constructor() {
        super();

        this.state = {
            artistQuery: '',
            artistName: '',
            followers: '',
            imageUrl:'',
            spotifyID:'',
            queryResult: {},
            genres:[],
            loaded:false


            // this.foo2 = this.foo2.bind(this)
        }

    }
updateArtistQuery = event=> {
console.log ('event', event.target.value);
this.setState({artistQuery: event.target.value})

}

searchArtist = () => {

    //http://172.31.89.85:5001/Artist?name=mick%20jagger
    //console.log ("button clicked")

    /*
         fetch ("http://www.boredapi.com/api/activity/")
            .then (response=>response.json())
            .then(json=>this.foo2(json))
         */


    console.log ("searchArtist() artist query",  this.state.artistQuery)
    let name = this.state.artistQuery
    //let GET_ARTIST_URL =  "http://172.31.89.85:5001/Artist?name="+name
    let GET_ARTIST_URL =  "http://localhost:5001/Artist?name="+name
    console.log(GET_ARTIST_URL)
    fetch (GET_ARTIST_URL)
        // .then (response=>this.foo2(response))
        .then (response=>response.json())
        //.then (json=>console.log(json))
        .then (json=>this.foo2(json))
        //.then (json=>this.setState({queryResult:json}))


}

    foo2(artist) {

       console.log(artist)


/*
        for (let key in artists){
            console.log(artists[key])
           // console.log ( key.name)

        }
*/
        //this.setState({queryResult:artists})
        //this.setState({queryResult:['a', 'b', 'c', 'd', 'e', 'f','g']})

        //let info =this.state.queryResult
        //{"image_url":"","name":"","spotify_id":"","total_followers":56146}
        const {image_url, name, spotify_id, total_followers}=artist
        let genres =artist.genres
       // artistName: '',
        this.setState({artistName:name})
        //    followers: '',
        this.setState ({followers:"Followers: " + total_followers})
        //    url:'',
        //    queryResult: {}


        this.setState({queryResult:artist})
        this.setState({imageUrl:image_url})
        this.setState({spotifyID:spotify_id})
        this.setState({genres:genres})
        this.setState({loaded:true})



        //return undefined;
    }

  
/*
handleKeyPress = event => {

   // this.setState({artistName:event.target.value}) // useless for now
    this.setState({artistQuery: event.target.value})
    if (event.key=='Enter'){

        console.log ('event', event.target.value);
       // this.setState({artistQuery: event.target.value})
      //  this.searchArtist()


    }
}
*/
  render(){
        return (
            <div className="App">
                <h2>Music Master</h2>
              <input onChange={this.updateArtistQuery}
              placeholder='Search for an artist'
              />

                <button onClick={this.searchArtist}>Search</button>



                {
                    this.state.loaded   ?
                    <Artist
                    spotifyID={this.state.spotifyID}
                    name={this.state.artistName}
                    info={this.state.queryResult}
                    followers={this.state.followers}
                    genres={this.state.genres}
                    imageUrl={this.state.imageUrl}

                    />
                :
                    ""
                }
            </div>
        );
    }
}
export default App;

