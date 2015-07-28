var assert     = require('assert');
var rewire     = require('rewire');
var User       = rewire('../src/user.js');
var bcryptMock = require('./bcrypt-mock.js');

describe('User', function () {

    before(function () {
//        User.__set__('bcrypt', bcryptMock);
    });

    describe('Password', function () {

        it('can be initially set without knowing the old password', function (done) {
            var user = new User();
            user.changePassword(undefined, 'secret', function () {
                assert.notEqual(user.password, undefined);
                done(); 
            });
        });

        it('throws exception if new password is not provided', function (done) {
            var user = new User();
            user.changePassword(undefined, undefined, function (err) {
                assert.equal(err.message.match(/same/) !== null, true);
                done();
            });
        });

        it('throws exception if new password is too short', function (done) {
            var user = new User();
            user.changePassword(undefined, 'short', function (err) {
                assert.equal(err.message.match(/short/) !== null, true);
                done();
            });
        });

        it('can only be changed if old password is provided', function (done) {
            var user = new User();
            user.changePassword(undefined, 'fishyfishy', function () {
                user.changePassword(undefined, 'doggydoggy', function (err) {
                    assert.equal(err.message.match(/provide/) !== null, true);
                    done(); 
                }); 
            });
        });

        it('should be encrypted', function (done) {
            var user = new User();
            var unencrypted = 'secret';
            var encrypted   = user.encryptPassword(unencrypted, function () {
                assert.notEqual(encrypted, unencrypted);
                done(); 
            });
        });

        it('should be comparable to check its authenticity', function (done) {
            var user = new User();
            user.changePassword(undefined, 'hello-world', function (err) {
                user.checkPassword('hello-world', function (err, same) {
                    assert.equal(same, true);
                    done();
                });
            });
        });
    });
});
