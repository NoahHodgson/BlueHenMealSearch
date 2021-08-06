const express = require('express');
const app = express();
const http = require('http');
var publicDir = require('path').join(__dirname,'/public');
app.use('/static', express.static(publicDir));
const server = http.createServer(app);

const { Server } = require("socket.io");
const io = new Server(server);

const csv = require('csvtojson');










app.get('/', (req, res) => {
    try{
        res.sendFile(publicDir + "/index.html");
        //res.send("<p>This is a test</p>");
    }
    catch(err){
        res.send('<p>404: Page Not Found</p>');
        console.log(err);
    }
});

io.on('connection', (socket) =>{
    console.log("A user connected.");
    socket.on('disconnect', () =>{
        console.log('A user disconnected. ');
    });
    socket.on('mealRequest', (msg)=>{
        console.log("mealRequest has been called");
        socket.emit("meals", [{ 'name': 'Chicken Salad1', 'location': 'Pencader1' }, { 'name': 'Chicken Parm1', 'location': 'Pencader1' }]);

    });
});

server.listen(3000, () =>{
    console.log("Listening on 3000");
});