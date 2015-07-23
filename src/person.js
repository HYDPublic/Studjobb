'use strict';

class Person {
    constructor () {
        this._email;
        this._firstName;
        this._lastName;
    }
    
    get email () {

    }

    set email (email) {
        if (email.split('@').length !== 2)
            throw new Error('Invalid email.');
    }

    get name () {
        var firstName = this._firstName || '';
        var lastName  = this._lastName  || '';
        var name      = (firstName + ' ' + lastName).trim()
        return (name ? name : 'Ukjent navn');
    }

    set firstName (firstName) {
        this._firstName = firstName;
    }

    set lastName (lastName) {
        this._lastName = lastName;
    }
}

module.exports = Person;
