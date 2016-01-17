// I have always had this phobia of working with oAuth. After getting asked a question on LinkedIn's oAuth2.0 implementation
// I decided that maybe I should figure out how it worked from a high level perspective. 

// 1. Authorize
// 2. Receive code and state 
// 3. Check state to prevent csrf attacks
// 4. Trade code for access token
// 5. Include access token in all future API calls
// 6. Refresh token after x period

var Linkedin = require('node-linkedin')('77925pmyp6icxs', '9toiR0WW3OwRgAgT', 'http://localhost:3000/oauth/linkedin/callback');
var express = require('express')

var app = express();
app.set('port', (process.env.PORT || 3000));

// Dummy token
var linkedin = Linkedin.init('my_access_token');

// Refer to site for full list of scopes available
var scope = ['r_basicprofile', 'r_emailaddress']

// Authorization 
app.get('/oauth/linkedin', function(req, res) {
    // This will ask for permisssions etc and redirect to callback url.
    Linkedin.auth.authorize(res, scope);
});

// Trade auth code for access token. 
// Middleware checks for state (private method)
app.get('/oauth/linkedin/callback', function(req, res) {
    Linkedin.auth.getAccessToken(res, req.query.code, req.query.state, function(err, results) {
        if ( err )
            return console.error(err);
 
        /**
         * Results have something like:
         * {"expires_in":5184000,"access_token":". . . ."}
         */
 
        console.log(results);
        return res.redirect('/');
    });
});


app.get('/', function(req, res) {
res.json({ message: 'eff off' });   
});

app.listen(app.get('port'), function() {
console.log('Node app is running on port', app.get('port'));
});