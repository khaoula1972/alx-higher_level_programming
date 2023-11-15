#!/usr/bin/node

const { dict } = require('./101-data');

const userByOccurrence = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  userByOccurrence[occurrences] = userByOccurrence[occurrences] || [];

  userByOccurrence[occurrences].push(parseInt(userId));
}

console.log(userByOccurrence);
