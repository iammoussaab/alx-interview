#!/usr/bin/node

import request from "request";

const id = process.argv[2];
const url = "https://swapi-api.hbtn.io/api/films/";

request(url + id, function (err, res, body) {
  if (err) throw err;

  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
