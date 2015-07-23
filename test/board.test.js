var assert = require('assert');
var Job    = require('../src/job.js');
var Board  = require('../src/board.js');

describe('Board', function () {
    
    describe('Jobs', function () {

        it('can be added to the board', function () {
            var board = new Board();
            var job   = new Job();
            board.jobs = job;
            assert.equal(board.jobs.length, 1);
        });

        it('should be filtered out if expired', function () {
            var board = new Board();
            var job   = new Job();
            var yesterday = new Date(+new Date() - 864e5);
            job.applicationDueDate = yesterday;
            board.jobs = job;
            assert.equal(board.jobs.length, 0);
        });
        
    });

});
