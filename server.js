//var http = require('http');  
//var fs = require('fs');  


var express = require("express");
var app = new express();
var publicDir = require('path').join(__dirname,'/public');
app.use(express.static(publicDir));

app.get('/',function(request,response){
    response.sendFile("/public/index.html");

});

app.listen(8000);
