module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'opening ACS zone add form': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/acs')
            .waitForElementVisible('button[ng-click="openACSZoneAddModal()"]', 2000)
            .click('button[ng-click="openACSZoneAddModal()"]')
    },
    'testing ACS zone add form': function (browser) {
        browser
            .waitForElementVisible('input[id="id_name"]', 2000)
            .waitForElementVisible('select[id="id_manager"]', 2000)
            .waitForElementVisible('textarea[id="id_description"]', 2000)
            .waitForElementVisible('button[ng-click="ok()"]', 2000)

            .setValue('input[id="id_name"]', 'Zone name')
            .setValue('select[id="id_manager"]', [browser.Keys.DOWN_ARROW])
            .setValue('textarea[id="id_description"]', 'Zone description')

            .click('button[ng-click="ok()"]')
    },
    'testing new zone visibility': function (browser) {
        browser
            .useXpath()
            .waitForElementVisible("//td[text()='Zone name']", 2000)
            .waitForElementVisible("//td[text()='Zone description']", 2000)
            .useCss()
            .pause(500)
            .end()
    }
};