module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'opening key overview page': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/keys')
    },
    'accepting request': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="deleteOrder(order.id)"]', 2000)
            .click('button[ng-click="deleteOrder(order.id)"]')
            .pause(500)
            .end()
    }
};