'use strict';
var Person = require('./person.js');
var bcrypt = require('bcrypt');

class User extends Person {
    constructor () {
        super();
        this._password;
    }
    
    get password () {
        return this._password;
    }

    changePassword (oldPassword, newPassword) {
        if (this.alreadyHasPassword()
        &&  this.encryptPassword(oldPassword) !== this._password)
            throw new Error('You must provide the old password to do that.');

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

    alreadyHasPassword () {
        return (this._password !== undefined);
    }

    encryptPassword (password) {
        return password === undefined
            ? undefined
            : password.split('').reverse().join('');
    }
}

module.exports = User;
