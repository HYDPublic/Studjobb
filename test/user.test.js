var assert = require('assert');
var User = require('../src/user.js');

describe('User', function () {
    describe('Password', function () {

        it('can be initially set without knowing the old password', function () {
            var user = new User();
            user.changePassword(undefined, 'secret');
            assert.equal(user.password, user.encryptPassword('secret'));
        });

        it('throws exception if new password is not provided', function () {
            var user = new User();
            assert.throws(function () {
                user.changePassword(undefined, undefined);
            }, /provided/);
        });

        it('throws exception if new password is too short', function () {
            var user = new User();
            assert.throws(function () {
                user.changePassword(undefined, 'short');
            }, /short/);
        });

        it('throws exception if new password is same as old password', function () {
            var user = new User();
            user.changePassword(undefined, 'fishyfishy');
            assert.throws(function () {
                user.changePassword(undefined, 'fishyfishy');
            }, /same/);
        });

        it('should be encrypted', function () {
            var user = new User();
            var unencrypted = 'secret';
            var encrypted   = user.encryptPassword(unencrypted);
            assert.notEqual(encrypted, unencrypted);
        });
    });

});
