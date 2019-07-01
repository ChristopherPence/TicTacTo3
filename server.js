const express = require('express');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const spawn = require("child_process").spawn;

//Load all of the env variables
require('dotenv').config();
const port = process.env.PORT;

let f = [ [2,0,0], [0,0,0], [0,0,0] ];
let m = [ [2,0,0], [0,1,0], [0,0,0] ];
let b = [ [2,0,0], [0,0,1], [0,0,0] ];

app.get('/play', function(req, res){

	var child = spawn('python', ["./win.py", JSON.stringify(f),JSON.stringify(m),JSON.stringify(b)]);

	child.stdout.on('data', function(data){
		res.send(data.toString());
	});

	child.stderr.on('data', function(data){
		console.log(data.toString());
	});
});




//listen on the right port
app.listen(port, function(){
	console.log('Server started on ' + port);
});