#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
	let max = process.argv[2];
	for (let i = 2; i < process.argv.length; i++) {
		if (process.argv[i] > max) {
          scd_max = max;
	      max = process.argv[i];
		}
	}
	console.log(scd_max);
}
