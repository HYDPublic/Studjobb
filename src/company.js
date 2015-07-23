'use strict';
var fs = require('fs');

class Company {
    constructor () {
        this._logo;
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
}

module.exports = Company;
