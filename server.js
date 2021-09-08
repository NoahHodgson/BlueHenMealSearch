var express = require('express');
var socket = require('socket.io');
var cors = require('cors')
var csv = require('csvtojson');

//App setup
var app = express();

var corsMiddleware = function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*'); //replace localhost with actual host
    res.header('Access-Control-Allow-Methods', 'OPTIONS, GET, PUT, PATCH, POST, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With, Authorization');
    next();
}

app.use(corsMiddleware);

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