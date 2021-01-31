#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const out = {};
    JSON.parse(body).forEach(task => {
      if (task.completed) {
        if (typeof out[task.userId] === 'undefined') {
          out[task.userId] = 0;
        }
        out[task.userId]++;
      }
    });
    console.log(out);
  }
});
