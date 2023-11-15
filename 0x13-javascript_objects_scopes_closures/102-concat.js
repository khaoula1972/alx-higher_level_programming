#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./concatFiles.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) throw err;

    const concatenatedData = data1 + data2;

    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
