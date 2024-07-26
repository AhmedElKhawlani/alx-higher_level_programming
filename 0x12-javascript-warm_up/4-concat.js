#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
    console.log("undefined is undefined")
}
else {
    if (args.length === 1) {
        let arg = args[0]
        let show = arg + " is undefined"
        console.log(show)
    }
    else {
        let arg1 = args[0]
        let arg2 = args[1]
        let show = arg1 + " is " + arg2
        console.log(show)
    }
}
