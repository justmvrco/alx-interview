#!/usr/bin/node
//  a script that prints all characters of a Star Wars movie Right order
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, function (err, response, body) {
  if (!err) {
    const urlchars = JSON.parse(body).characters;
    const len = urlchars.length;
    Names(0, urlchars[0], urlchars, len);
  }
});
function Names (i, url, chars, len) {
  if (i === len) {
    return;
  }
  request.get(url, function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      i++;
      Names(i, chars[i], chars, len);
    }
  });
}
