//var http = require('http');  
//var fs = require('fs');  
const {PythonShell} = require('python-shell');
const {spawn} = require('child_process');

function callScraper(){
    const python = spawn('python',['/MealScraper/main.py']);
    python.stdout.on('data', function(data)  {
        console.log("Getting data from python script");
        console.log(data);
    })
}

var express = require("express");
var app = new express();
var publicDir = require('path').join(__dirname,'/public');
app.use(express.static(publicDir));

app.get('/',function(request,response){
    console.log("In request");
    response.sendFile("/public/index.html");
    PythonShell.run(test.py, null,  function (err){
    if (err){
        throw err;
    }
    console.log('finished');

    });


});

app.listen(8000);
console.log("After listen");
let options = {
    mode: 'text',
    //pythonPath: '',
    pythonOptions: ['-u'],
    scriptPath: 'MealScraper/'
};
    PythonShell.run("main.py",options,  function (err, results){
    if (err){
        throw err;
    }
    console.log(results);
})
    console.log('finished');