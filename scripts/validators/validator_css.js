// Imports all modules from node_modules
const fs = require('fs');
const glob = require('glob');
const validator = require('css-validator');

/**
 * The array that contains all of the .css file paths
 */
let pathList = [];

/**
 * The function that fetches all of the directories excluding the "node_modules" folder but still including all .css files elsewhere
 */
glob("./public/**/*", async (error, /** @type {any[]} */ result) => {
    if (error) {
        console.log('Error', error);
    } else {
        // Loop through each directory and push it to a list of paths if the file is a .css file
        result.forEach(/** @param {any[]} */ item => {
            if (!item.includes("./node_modules") && item.includes(".css")) {
                pathList.push(item);
            }
        });
        await validate();
    }
});

/**
 * Validates all of the .css files in the pathList array
 * Returns either errors or a completion message for every .css file
 */
async function validate() {
    let anyErrors = false;
    let asyncIndex = 0;
    await asyncForEach(pathList, (filePath, _, list) => {
        // Fetches the file from the path into a String
        fs.readFile(filePath, 'utf8', async (err, /** @type {String} */ file) => {
            console.log("Reading file: " + filePath);
            if (err) { throw err; }
            // To check if there are any errors found in the loop
            validator(file, async function (err, /** @type {String[]} */data) {
                // If the file is valid or not
                if (data.validity == false) {
                    // To indicate that there's at least one error
                    anyErrors = true;
                    // Loop through all errors asynchronously and print them to the terminal
                    await asyncForEach(data.errors, (value, index, array) => {
                        // Errors
                        /**@type {Number} */
                        let line = value.line;
                        /**@type {String} */
                        let errorType = value.errorType;
                        /**@type {String} */
                        let context = value.context;
                        /**@type {String} */
                        let message = value.message;
                        message = message.replace(/\n/g, " ").replace(/  +/g, " ");
                        // The strange symbols are there for coloring the important text
                        console.log("\x1b[41m\x1b[30m", "Error at " + "line " + `${line} ` + "\x1b[0m", "in" + "\x1b[35m", `${filePath}` + "\x1b[0m", ", " + "\x1b[36m", `${context}` + "\x1b[0m", ", Error type: " + "\x1b[36m", `${errorType}` + "\x1b[0m", ". Message: " + "\x1b[0m", `${message}`);
                        console.log("");
                    });
                } else {
                    await asyncForEach(data.warnings, (value, index, array) => {
                        // Warnings
                        let line = value.line;
                        let warningType = value.warning.replace(/\n/g, " ").replace(/  +/g, " ");
                        let message = value.message;
                        // The strange symbols are there for coloring the important text
                        console.log("\x1b[43m\x1b[30m", "Warning at " + "line " + `${line} ` + "\x1b[0m", "in" + "\x1b[35m", `${filePath}` + "\x1b[0m", "Warning type: " + "\x1b[36m", `${warningType}` + "\x1b[0m", ". Message: " + "\x1b[0m", `${message}`);
                        console.log("");
                    });
                }
                // Because of the asynchronous nature of the parent validator function, the function will return information in different speeds. 
                // The index will then be out of order which is why we have created a new index variable
                asyncIndex++;
                // If "anyErrors" equals true and the loop has completed, the process will exit with an error
                if (asyncIndex == list.length && anyErrors) {
                    // Inserts a new line to make everything more readable
                    console.log("");
                    // When the loop has completed its last run and has found errors in the code
                    process.exit(1);
                } else if (asyncIndex == list.length && !anyErrors) {
                    console.log("All files are error and warning free and validate according to the specified schema");
                }
            });
        });
    });
}

/**
 * A function that goes through a list as foreach but asynchronously 
 * @param {any[]} list 
 * @param {Function} callback 
 */
async function asyncForEach(list, callback) {
    for (let index = 0; index < list.length; index++) {
        await callback(list[index], index, list);
    }
}