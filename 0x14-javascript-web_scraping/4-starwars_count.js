#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let out = 0;
    const list = JSON.parse(body);
    list.results.forEach(dict => {
      dict.characters.forEach(character => {
        if (character.includes('18')) {
          out++;
        }
      });
    });
    console.log(out);
  }
});
