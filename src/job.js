'use strict';

class Job {

    constructor () {
        this._title = 'Mangler tittel.';
        this._description = 'Mangler beskrivelse.';
        this._applicationDueDate = this.generateDateTwoWeeksFromNow();
    }

    get title () {
        return this._title;
    }

    set title (title) {
        title = this.capitalizeFirstCharacter(title);
        this._title = title;
    }

    get description () {
        return this._description;
    }

    get applicationDueDate () {
        return this._applicationDueDate; 
    }

    set applicationDueDate (applicationDueDate) {
        this._applicationDueDate = applicationDueDate;
    }

    get expired () {
        return (new Date() > this._applicationDueDate);
    }

    capitalizeFirstCharacter (stringToBeCapitalized) {
        return stringToBeCapitalized.charAt(0).toUpperCase() + stringToBeCapitalized.slice(1);
    }

    generateDateTwoWeeksFromNow () {
        return new Date(+new Date() + 12096e5); 
    }
}

module.exports = Job;
