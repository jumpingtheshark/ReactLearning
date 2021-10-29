import './App.css';
import React, {Component} from "react";
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
            queryResult: {}


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
       // artistName: '',
        this.setState({artistName:name})
        //    followers: '',
        this.setState ({followers:"Followers: " + total_followers})
        //    url:'',
        //    queryResult: {}


        this.setState({queryResult:artist})
        this.setState({imageUrl:image_url})



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


                <div>



<p>
                    {this.state.artistName}
</p>
                    <p>
                   {this.state.followers}
                    </p>

                    <image src={imageUrl}>

                    </image>


                </div>


            </div>
        );
    }
}
export default App;

