var app = require('express')();
    var https = require('https');
    var fs = require( 'fs' );
    var io = require('socket.io')(server);

    var options = {
        key: fs.readFileSync('./test_key.key'),
        cert: fs.readFileSync('./test_cert.crt'),
        ca: fs.readFileSync('./test_ca.crt'),

        requestCert: false,
        rejectUnauthorized: false
    }

    
    //Static files
app.use(express.static(__dirname + '/public'));


    var server = https.createServer(options, app);
    server.listen(8080, function(){
        console.log("Listening on port: 8080");
    });
    

    
    io.sockets.on('connection', function (socket) {
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
    
    app.get("/", function(request, response){
        // code goes here...
    })