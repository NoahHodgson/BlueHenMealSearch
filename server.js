var express = require('express');
var socket = require('socket.io');
//var csvtojson = require('csvtojson');

//App setup
var app = express();
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
        obj = [{'name':'Chicken Salad', 'location':'Pencader'},{'name':'Chicken Parm', 'location':'Pencader'}];
        socket.emit('meals', obj);
        console.log("Sent meal respone");

        

    });
    
    
    
    
    
    socket.on('disconnect', function(){
        console.log("User has disconnected");
    });
});