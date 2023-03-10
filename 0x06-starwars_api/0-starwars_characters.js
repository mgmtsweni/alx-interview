#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const args = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${args}`;

request(movieUrl, function (error, response, body) {
  if (!error) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    printChar(characters, 0);
  }
});

function printChar (url, index) {
  const eachCharurl = url[index];
  request(eachCharurl, function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < url.length) {
        printChar(url, index + 1);
      }
    }
  });
}
