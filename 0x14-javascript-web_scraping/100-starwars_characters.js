#!/usr/bin/node
const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    for (const charUrl of JSON.parse(body).characters) {
      request(charUrl, function (err2, response2, body2) {
        if (err2) {
          throw err2;
        } else {
          console.log(JSON.parse(body2).name);
        }
      });
    }
  }
});
