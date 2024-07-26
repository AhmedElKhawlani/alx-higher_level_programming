#!/usr/bin/node

const args = process.argv.slice(2);

if (JSON.stringify(args) === "[]") {
    console.log("No argument")
}
else {
    args.forEach(function(arg) {
        console.log(arg)
    })
}
