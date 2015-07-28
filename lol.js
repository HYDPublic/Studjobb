var bcrypt = require('bcrypt');

bcrypt.hash('hello-world', 10, function(err, hash) {
    bcrypt.compare('hello-world', hash, function(err, result) {
        console.log(result);
    });
});
