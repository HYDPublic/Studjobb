var assert = require('assert');
var Job    = require('../src/job.js');

describe('Job', function () {

    describe('title', function () {
        
        it('has a default value', function () {
            var job = new Job(); 
            assert.equal(typeof job.title, 'string');
        });

        it('can be set', function () {
            var job = new Job(); 
            job.title = 'Programmerer søkes!';
            assert.equal(job.title, 'Programmerer søkes!');
        });

        it('should have first character capitalized', function () {
            var job = new Job(); 
            job.title = 'programmerer søkes!';
            assert.equal(job.title, 'Programmerer søkes!');
        });

    });

    describe('Application due date', function () {

        it('should by default be set to 2 weeks in the future', function () {
            var job = new Job();
            var now = new Date();
            var twoWeeksInMilliseconds = 12096e5 - 50;
            assert.equal(job.applicationDueDate - now > twoWeeksInMilliseconds, true);
        });
    
        it('can be set to another date', function () {
            var job = new Job();
            var tomorrow = new Date(+new Date() + 864e5);
            job.applicationDueDate = tomorrow;
            assert.equal(job.applicationDueDate, tomorrow);
        });

        it('should be expired if set to date in the past', function () {
            var job = new Job();
            var now = new Date();
            var yesterday = new Date(+new Date() - 864e5); 
            job.applicationDueDate = yesterday;
            assert.equal(job.expired, true);
        });

        it('should not be expired if set to date in the future', function () {
            var job = new Job();
            var now = new Date();
            var tomorrow = new Date(+new Date() + 864e5); 
            assert.equal(job.expired, false);
        });
    });

    describe('Description', function () {
        
        it('must have a default description', function () {
            assert.equal(typeof new Job().description, 'string');
        });
        
        it('should be possible to set it', function () {
            var job = new Job();
            job.description = 'Fantastisk bra jobb.';
            assert.equal(job.description, 'Fantastisk bra jobb.');
        });

    });

    describe('Publication date', function () {
        
        it('should be possible to set it', function () {
            var job = new Job(); 
            var now = new Date();
            job.publicationDate = now;
            assert.equal(job.publicationDate, now);
        });
    });
});
