module.exports = {
    'testing person add form': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/users')
            .waitForElementVisible('button[ng-click="openPersonAddModal()"]', 2000)
            .click('button[ng-click="openPersonAddModal()"]')
            .waitForElementVisible('form[name=personAddForm]', 2000)
            .setValue('input[id="id_first_name"]', 'First name')
            .setValue('input[id="id_last_name"]', 'Last name')
            .setValue('select[id="id_rank"]', ['kapral', browser.Keys.RETURN])
            .setValue('input[id="id_card_number"]', '1111111111111')
            .setValue('select[id="id_group"]', [browser.Keys.DOWN_ARROW])
            .click('button[ng-click="ok()"]')
            .pause(500)
            .end()
    }
};