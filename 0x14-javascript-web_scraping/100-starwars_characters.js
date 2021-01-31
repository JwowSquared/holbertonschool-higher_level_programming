#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    JSON.parse(body).characters.forEach(character => {
      request(character, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
