import {renderToStaticMarkup} from "react-dom/server";

export class Dict {

foo() {
    let
        resultJson = {
            "name": "jagger",
            "followers": 1234
        }


    const {name, followers} = resultJson
    //console.log(resultJson)
    console.log(name)
    console.log(followers)

}

    foo2() {
        let resultJson = {
                "name": "jagger",
                "followers": 1234
            }

        const name = resultJson.name
        let {name2, followers }= resultJson

        console.log (name, name2)

        //console.log(resultJson)
       // console.log(name)
       // console.log(followers)

    }

    foo3()
    {
        let resultJson = {
            "name": "jagger",
            "followers": 1234,
            "band":["jagger", "richards", "watts"]
        }
        let band = resultJson.band
        console.log(band[2])

        for (let k in resultJson){
            console.log(k, resultJson[k] )

        }



    }



}