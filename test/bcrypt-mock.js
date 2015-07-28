var bcryptMock = {
    psuedoEncryption: function (stringToBeEncrypted) {
        return stringToBeEncrypted.split('').reverse().join();
    },

    hash: function (passwordToBeHashed, salt, done) {
        var psuedoHashedPassword = this.psuedoEncryption(passwordToBeHashed);
        done(undefined, psuedoHashedPassword);
    },

    compare: function (passwordToBeChecked, hash, done) {
        done(undefined, (hash === this.psuedoEncryption(passwordToBeChecked)));
    }
}

module.exports = bcryptMock;
