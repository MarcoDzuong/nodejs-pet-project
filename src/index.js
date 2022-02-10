import http from 'http';
import express from 'express';
import cors from 'cors';
import morgan from 'morgan';
import bodyParser from 'body-parser';
import middleware from './middleware';
import config from './config/config.json';

require('./bootstrap');
require('dotenv').config();

let app = express();
const AsyncFunction = (async () => {}).constructor;

//Catch all unhandled error in try-catch function
let wrap = fn => (...args) => {
	if (fn instanceof AsyncFunction) {
		return fn(...args);
	} else {
		return fn(...args).catch(args[2]);
	}
}

app.server = http.createServer(app);

// logger
app.use(morgan('dev'));

// 3rd party middleware
app.use(cors({
	exposedHeaders: config.corsHeaders
}));

app.use(bodyParser.json({
	limit: config.bodyLimit
}));

// internal middleware
app.use(middleware({ config }));

// api router
const apiVersion = config.apiVersion;
const api = require(`./api/${apiVersion}`).default;
app.use(`/api/${apiVersion}`, wrap(api({ config })));

app.use(function (err, req, res, next) {
	if (res.headersSent) {
		return next(err)
	}
	console.log(err);
	res.status(500).send('INTERNAL SERVER ERROR !');
});

app.server.listen(process.env.PORT || config.port, () => {
	console.log(`Started on port ${app.server.address().port}`);
});

export default app;