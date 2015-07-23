var assert  = require('assert');
var path    = require('path');
var Job     = require('../src/job.js');
var Company = require('../src/company.js');

describe('Company', function () {
    
    describe('Logo', function () {
        it('must exist as a file', function () {
            var company  = new Company();
            var logoPath = path.join(__dirname, 'fixtures', 'exists.png');
            company.logo = logoPath;
            assert.equal(company.logo, logoPath);
        });

        it('throws exception if file does not exist', function () {
            var company  = new Company();
            var logoPath = path.join(__dirname, 'fixtures', 'does-not-exist.png');
            assert.throws(function () {
                company.logo = logoPath;
            });
        });
    });
});
