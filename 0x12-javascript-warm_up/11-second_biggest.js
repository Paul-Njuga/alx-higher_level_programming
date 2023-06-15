#!/usr/bin/node
/**
 * Slice two to rmv node & path
 * Map it to Number for typecasting
 */
const args = process.argv.slice(2).map(Number);

function scdLrg (args) {
  /* -Infinity is the least possible value */
  let max = -Infinity;
  let scdMax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      scdMax = max;
      max = args[i];
    } else if (args[i] > scdMax && args[i] < max) {
      scdMax = args[i];
    }
  }
  return scdMax;
}

if (args.length < 2) {
  console.log(0);
} else {
  const scndLarge = scdLrg(args);
  console.log(scndLarge);
}
