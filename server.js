//var http = require('http');  
//var fs = require('fs');  
var express = require("express");
const {spawn} = require("child_process");
port = 8000




var app = new express();
var publicDir = require('path').join(__dirname,'/public');
app.use(express.static(publicDir));

app.get('/',function(request,response){
    response.sendFile("/public/index.html");

});

var dataToSend;
const python = spawn("python", [""]);
python.stdout.on("data", function (data) {
    console.log();
    dataToSend = data.toString();
});

python.on("close", (code) => {
    console.log("Child process closed, sending data. ");
});

app.listen(port);
