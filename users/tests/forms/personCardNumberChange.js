module.exports = {
    'testing person data change form': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/person_detail/3')
            .waitForElementVisible('button[ng-click="updateCardNumber()"]', 5000)
            .setValue('input[id="id_card_number"]', [
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                browser.Keys.BACK_SPACE,
                '2222222222'])
            .click('button[ng-click="updateCardNumber()"]')
            .pause(2000)
            .end()
    }
};