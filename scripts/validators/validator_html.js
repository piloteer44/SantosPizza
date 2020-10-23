// Imports all modules from node_modules
const fs = require('fs');
const glob = require('glob');
const validator = require('html-validator');

/**
 * The array that contains all of the .css file paths
 */
let pathList = [];

/**
 * The function that fetches all of the directories excluding the "node_modules" folder but still including all .html files elsewhere
 */
glob("./public/**/*", (error, /** @type {any[]} */ result) => {
    if (error) {
        console.log('Error', error);
    } else {
        // Loop through each directory and push it to a list of paths if the file is a .html file
        result.forEach(/** @param {any[]} */ item => {
            if (!item.includes("./node_modules") && item.includes(".html")) {
                pathList.push(item);
            }
        });
        validate();
    }
});

/**
 * Validates all of the .html files in the pathList array
 * Returns either errors or a completion message for every .html file
 */
function validate() {
    let anyErrors = false;
    let asyncIndex = 0;
    pathList.forEach((filePath, _, list) => {
        // Fetches the file from the path into a String
        fs.readFile(filePath, 'utf8', async (err, /** @type {String} */ file) => {
            console.log("Reading file: " + filePath);
            if (err) { throw err; }
            // To check if there are any errors found in the loop
            // Fetches the validity of the .html file asynchronously
            const data = await validator({ data: file, format: "text" });
            // If the file is valid or not
            if (data.includes("Error")) {
                // To indicate that there's at least one error
                anyErrors = true;
                // Print all errors to the terminal
                console.log(data);
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
            } else if(asyncIndex == list.length && !anyErrors){
                console.log("All files are error and warning free and validate according to the specified schema");
            }
        });
    });
}