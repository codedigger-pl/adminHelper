module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'opening key add form': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/keys')
            .waitForElementVisible('button[ng-click="openKeyAddModal()"]', 2000)
            .click('button[ng-click="openKeyAddModal()"]')
    },
    'testing key add form': function (browser) {
        browser
            .waitForElementVisible('input[id="id_name"]', 2000)
            .waitForElementVisible('select[id="id_manager"]', 2000)
            .waitForElementVisible('textarea[id="id_description"]', 2000)
            .waitForElementVisible('button[ng-click="ok()"]', 2000)

            .setValue('input[id="id_name"]', 'Key name')
            .setValue('select[id="id_manager"]', [browser.Keys.DOWN_ARROW])
            .setValue('textarea[id="id_description"]', 'Key description')

            .click('button[ng-click="ok()"]')
    },
    'testing new key visibility': function (browser) {
        browser
            .useXpath()
            .waitForElementVisible("//td[text()='Key name']", 2000)
            .waitForElementVisible("//td[text()='Key description']", 2000)
            .useCss()
            .pause(500)
            .end()
    }
};