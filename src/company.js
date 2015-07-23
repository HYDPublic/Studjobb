'use strict';
var fs = require('fs');

class Company {
    constructor () {
        this._logo;
        this._jobs = [];
    }
    
    get logo () {
        return this._logo;
    }

    set logo (pathToLogo) {
        if (fs.existsSync(pathToLogo))
            this._logo = pathToLogo; 
        else
            throw new Error('Logo does not exist.');
    }

    get jobs () {
        return this._jobs;
    }

    set jobs (job) {
        this._jobs.push(job);
    }
}

module.exports = Company;
