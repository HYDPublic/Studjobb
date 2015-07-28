'use strict';
var Person = require('./person.js');
var bcrypt = require('bcrypt');
var async  = require('async');

class User extends Person {

    constructor () {
        super();
        this._password;
    }
    
    get password () {
        return this._password;
    }

    changePassword (oldPassword, newPassword, done) {
        var self = this;

        async.map([oldPassword, newPassword], self.encryptPassword,
        function (err, encryptedPasswords) {

            var oldPasswordEncrypted = encryptedPasswords[0];
            var newPasswordEncrypted = encryptedPasswords[1];

            async.map([oldPassword, newPassword], self.checkPassword,
            function (err, checkedPasswords) {
                console.log(err);

                try {
                    self.isValidPassword(newPassword);
                } catch (err) {
                    return done(err);
                }
                
                self._password = newPasswordEncrypted; 

                return done();
            });
        });
    }

    isValidPassword (password) {
        if (password === undefined)
            throw new Error('New password not provided.');
        
        if (password.length < 6)
            throw new Error('New password is too short.');

        return true;
    }

    checkPassword (passwordToCheck, done) {
        bcrypt.compare(passwordToCheck, self._password || '', done);
    }

    alreadyHasPassword () {
        return (this._password !== undefined);
    }

    encryptPassword (password, done) {
        if (password === undefined)
            return done(undefined, undefined);
        
        bcrypt.hash(password, 10, done);
    }
}

module.exports = User;
