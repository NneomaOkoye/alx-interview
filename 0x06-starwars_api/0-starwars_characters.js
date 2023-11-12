#!/usr/bin/node
// make request to star wars api

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films';

const movie = process.argv.slice(2)[0];

// handle api requests using request module
const apiRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
};

// main function
const makeRequest = async () => {
  try {
    const response = await apiRequest(`${apiUrl}/${movie}`);
    const data = JSON.parse(response);
    const characters = data.characters;
    for (const characterUrl of characters) {
      const res = await apiRequest(characterUrl);
      const character = JSON.parse(res);
      console.log(character.name);
    }
  } catch (err) {
    console.log(err);
  }
};

makeRequest();
