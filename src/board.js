'use strict';

class Board {
    constructor () {
        this._jobs = [];
    }

    set jobs (job) {
        this._jobs.push(job);
    }

    get jobs () {
        return this.filterOutExpiredJobs();
    }

    filterOutExpiredJobs () {
        return this._jobs.filter(function (job) {
            return job.expired === false;
        });
    }
}

module.exports = Board;
