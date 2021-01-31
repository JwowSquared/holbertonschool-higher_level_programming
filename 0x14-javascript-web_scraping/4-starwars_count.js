#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let out = 0;
    const list = JSON.parse(body);
    list.results.forEach(dict => {
      if (dict.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        out++;
      }
    });
    console.log(out);
  }
});
