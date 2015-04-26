module.exports = {
    'testing login form': function (browser) {
        browser
            .login('test_user', 'test_user')
            .pause(500)
            .assert.urlEquals('http://127.0.0.1:8081/#/users')
            .end()
    }
};