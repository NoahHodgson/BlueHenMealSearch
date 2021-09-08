var express = require('express');
var socket = require('socket.io');
var cors = require('cors')
var csv = require('csvtojson');

//App setup
var app = express();

app.use((req, res, next) => {
    //allow access from every, elminate CORS
    res.setHeader('Access-Control-Allow-Origin','*');
    res.removeHeader('x-powered-by');
    //set the allowed HTTP methods to be requested
    res.setHeader('Access-Control-Allow-Methods','POST');
    //headers clients can use in their requests
    res.setHeader('Access-Control-Allow-Headers','Content-Type');
    //allow request to continue and be handled by routes
    next();
  });
  
var server = app.listen(8000, function(){
    console.log("Listening to requests on port 8000");
});

//Static files
app.use(express.static(__dirname + '/public'));

//Socket setup
var io = socket(server);

io.on('connection', function(socket){
    console.log("Made a socket connection -- Socket id: ", socket.id, " -- IP: ", socket.request.connection.remoteAddress);

    //Send current meals to the client
    socket.on('requestMeals', function(input){
        console.log("Received meal request");
        obj = {}
        csv().fromFile(__dirname+"/MealScraper/results.csv")
        .then(function(jsonArrayObject){
            //console.log(jsonArrayObject);
            socket.emit('meals',jsonArrayObject);
        });
        //obj = [{'name':'Chicken Salad', 'location':'Pencader'},{'name':'Chicken Parm', 'location':'Pencader'}];
        //console.log(obj);
        //socket.emit('meals', obj);
        console.log("Sent meal respone");

        

    });
    
    
    
    
    
    socket.on('disconnect', function(){
        console.log("User has disconnected");
    });
});