#!/usr/bin/node
const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
const request = require('request');
function retrive (urlChar) {
  return new Promise(function (resolve, reject) {
    request(urlChar, function getChar (err2, response2, body2) {
      if (err2) {
        reject(err2);
      } else {
        resolve(JSON.parse(body2).name);
      }
    });
  });
}
async function getlist (urlist) {
  for (const urlChar of urlist) {
    const character = await retrive(urlChar);
    console.log(character);
  }
}

request(url, function getList (err, response, body) {
  if (err) {
    throw err;
  } else {
    const urlist = JSON.parse(body).characters;
    getlist(urlist);
  }
});
