var express = require('express');
var cors = require('cors')
var csv = require('csvtojson');

//App setup
var app = express();

app.use(cors());

var server = app.listen(80, function(){
    console.log("Listening to requests on port 80");
});
var io = require('socket.io')(server,{
    cors:{
        origin:"*",
        methods: ["GET", "POST"]
    }
    });

//Static files
app.use(express.static(__dirname + '/public'));

//Socket setup

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
