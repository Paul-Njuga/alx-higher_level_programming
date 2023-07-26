#!/usr/bin/node
/* Computes the number of tasks completed by user id */
const args = process.argv.slice(2);

if (args.length === 1) {
  const url = args[0];
  const obj = {};
  const request = require('request');
  request(url, function (error, _, body) {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body);
      for (const td of data) {
        if (td.completed) {
          obj[td.userId] ? obj[td.userId]++ : (obj[td.userId] = 1);
        }
      }
      console.log(obj);
    }
  });
} else {
  console.log('Usage: ./6-completed_tasks.js URL');
}
