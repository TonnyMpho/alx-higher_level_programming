#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, res, body) => {
	if (error) {
		console.log(error);
	} else {
		fs.writeFileSync(file, body, 'utf-8', error => {
			console.log(error);
		})
	}
})
