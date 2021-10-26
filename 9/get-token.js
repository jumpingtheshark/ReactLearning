const request = require('request');
console.log ('hi')

var client_id = '3032d7618ce34dffaf349214bba92cd5';
var client_secret = 'a6bf34e7fc4b4066991b3d344f465a3f';

var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    headers: {
        'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
    },
    form: {
        grant_type: 'client_credentials'
    },
    json: true
};
let token2 = ''
request.post(authOptions, function(error, response, body) {
    if (!error && response.statusCode === 200) {
        var token = body.access_token;
        token2=token
        console.log(token)
        let authOptions2 = {
            url: 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V',
            headers: {
                'Authorization': 'Bearer ' + token2}
        };

        request.get(authOptions2, function(error, response, body){
                console.log(response.statusCode)
                console.log(response.body)
                //console.log(response.json())
                console.log(response.body)
            }


        )

    }
    else {
        console.log('problem')
        console.log(error)
        console.log(response.statusCode)
    }
});
