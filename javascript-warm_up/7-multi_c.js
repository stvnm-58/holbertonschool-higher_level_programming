#!/usr/bin/node

const myVar = parseInt(process.argv[2]);


if (isNaN(myVar) == true) {
    console.log("Missing number of occurences");
}

else {
    for (let i = 0; i < myVar; i++) {
        console.log("C is fun");
    }
}
