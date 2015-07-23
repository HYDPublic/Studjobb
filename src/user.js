'use strict';
var Person = require('./person.js');

class User extends Person {
    constructor () {
        super();
        this._password;
    }
    
    get password () {
        return this._password;
    }

    changePassword (oldPassword, newPassword) {
        if (this.isValidPassword(newPassword))
            this._password = this.encryptPassword(newPassword); 
    }

    isValidPassword (password) {
        if (password === undefined)
            throw new Error('New password not provided.');
        
        if (password.length < 6)
            throw new Error('New password is too short.');

        if (this._password === this.encryptPassword(password))
            throw new Error('New password same as old one.');

        return true;
    }

    encryptPassword (password) {
        return password.split('').reverse().join('');
    }
}

module.exports = User;
