module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'testing user add form': function (browser) {
        browser
            .url('http://127.0.0.1:8081/#/users')
            .waitForElementVisible('button[ng-click="openUserAddModal()"]', 2000)
            .click('button[ng-click="openUserAddModal()"]')
            .waitForElementVisible('form[name=userAddForm]', 2000)
            .setValue('input[id="id_username"]', 'username')
            .setValue('input[id="id_first_name"]', 'First name')
            .setValue('input[id="id_last_name"]', 'Last name')
            .setValue('select[id="id_rank"]', ['kapral', browser.Keys.RETURN])
            .setValue('input[id="id_email"]', 'user@user.com')
            .click('button[ng-click="ok()"]')
            .pause(500)
            .end()
    }
};