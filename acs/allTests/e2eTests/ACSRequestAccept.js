module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'opening ACS overview page': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/acs')
    },
    'accepting request': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="acceptRequest(request.id)"]', 2000)
            .click('button[ng-click="acceptRequest(request.id)"]')
            .pause(500)
            .end()
    }
};