module.exports = {
    'testing person data change form': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/person_detail/2')
            .waitForElementVisible('button[ng-click="updateData()"]', 2000)
            .setValue('input[id="id_first_name"]', [
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
                'New first name'])
            .setValue('input[id="id_last_name"]', [
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
                'New last name'])
            .setValue('select[id="id_rank"]', ['pan', browser.Keys.RETURN])
            .setValue('input[id="id_card_number"]', '1111111111111')
            .setValue('select[id="id_group"]', [browser.Keys.DOWN_ARROW, browser.Keys.DOWN_ARROW])
            .click('button[ng-click="updateData()"]')
            .pause(500)
            .end()
    }
};