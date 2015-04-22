module.exports = {
    'opening alarm zone add form': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/alarm')
            .waitForElementVisible('button[ng-click="openAlarmOrderAddModal()"]', 2000)
            .click('button[ng-click="openAlarmOrderAddModal()"]')
    },
    'testing alarm zone add form': function (browser) {
        browser
            .waitForElementVisible('select[id="id_zone"]', 2000)
            .waitForElementVisible('select[id="id_person"]', 2000)
            .waitForElementVisible('select[id="id_user"]', 2000)
            .waitForElementVisible('input[id="id_grant_privilege"]', 2000)
            .waitForElementVisible('button[ng-click="ok()"]', 2000)

            .setValue('select[id="id_zone"]', [browser.Keys.DOWN_ARROW])
            .setValue('select[id="id_person"]', [browser.Keys.DOWN_ARROW])
            .setValue('select[id="id_user"]', [browser.Keys.DOWN_ARROW])
            .click('input[id="id_grant_privilege"]')

            .click('button[ng-click="ok()"]')
    },
    'testing new order visibility': function (browser) {
        browser
            .useXpath()
            .waitForElementVisible("//td[text()='Nadanie uprawnienia']", 2000)
            .useCss()
            .pause(500)
            .end()
    }
};