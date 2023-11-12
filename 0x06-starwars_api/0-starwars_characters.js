#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));

const filmId = process.argv[2];

async function main(id) {
  try {
    const filmEndpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
    let filmResponse = await request(filmEndpoint);
    const filmData = JSON.parse(filmResponse.body);
    const characters = filmData.characters;

    for (const characterEndpoint of characters) {
      let characterResponse = await request(characterEndpoint);
      const characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main(filmId);
