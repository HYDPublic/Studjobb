var assert = require('assert');
var Person = require('../src/person.js');

describe('Person', function () {
    
    describe('Name', function () {
        it('should consist of a first name and a last name', function () {
            var person = new Person();
            person.firstName = 'Michael';
            person.lastName = 'McMillan';
            assert.equal(person.name, 'Michael McMillan');
        });

        it('should only return first name if no last name is provided', function () {
            var person = new Person();
            person.firstName = 'Michael';
            assert.equal(person.name, 'Michael');
        });

        it('should only return the last name if no first name is provided', function () {
            var person = new Person();
            person.lastName = 'McMillan';
            assert.equal(person.name, 'McMillan');
        });

        it('should by default equal to unknown name', function () {
            var person = new Person();
            assert.notEqual(person.name, '');
            assert.equal(typeof person.name, 'string');
        });
    });

    describe('Email', function () {
        it('throws exception if @ is not present', function () {
            var person = new Person();
            assert.throws(function () {
                person.email = 'email(at)email(dot)com';
            });
        });

        it('does not throw exception if @ is present', function () {
            var person = new Person();
            assert.doesNotThrow(function () {
                person.email = 'email@email(dot)com';
            });
        });

        it('throw exception if @ is present more than once', function () {
            var person = new Person();
            assert.throws(function () {
                person.email = 'email@@email(dot)com';
            });
        });
    });

});
