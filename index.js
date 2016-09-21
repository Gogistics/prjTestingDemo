var express = require('express'),
    bodyParser = require('body-parser'),
    check = require('./my_modules/check.js');
 
var app = express();
app.use(bodyParser.json());
 
app.get('/', function (req, res) {
  res.send('Strider/Nodejs Demo');
});

app.get('/user', function(req, res) {
  res.status(200).json({ first_name: 'Allen', last_name: "Tai" });
});

app.post('/is-prime', function(req, res){
  var info = req.body;
  res.status(200).json({is_prime: check.isPrime(info.num)});
});
 
app.listen(process.env.PORT || 5000);
 
module.exports = app;
