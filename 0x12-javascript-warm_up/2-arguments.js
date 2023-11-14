#!/usr/bin/node

// A script that prints a message depending of the number of arguments passed

// Check the number of arguments
const numArgs = process.argv.length - 2;

// Print message based on the number of arguments
if (numArgs === 0) {
  console.log("No argument");
} else if (numArgs === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
