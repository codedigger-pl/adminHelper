module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'testing person add form': function (browser) {
        browser
            // going to overview page
            .url('http://127.0.0.1:8081/#/users')
            .waitForElementVisible('button[ng-click="openPersonAddModal()"]', 2000)
            .click('button[ng-click="openPersonAddModal()"]')

            // checking visibility
            .waitForElementVisible('form[name=personAddForm]', 2000)
            .waitForElementVisible('input[id="id_first_name"]', 2000)
            .waitForElementVisible('input[id="id_last_name"]', 2000)
            .waitForElementVisible('select[id="id_rank"]', 2000)
            .waitForElementVisible('input[id="id_card_number"]', 2000)
            .waitForElementVisible('select[id="id_group"]', 2000)
            .waitForElementVisible('button[ng-click="ok()"]', 2000)

            // filling form
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