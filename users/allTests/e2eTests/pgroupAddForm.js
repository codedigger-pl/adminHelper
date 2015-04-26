module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'testing person group add form': function (browser) {
        browser
            .url('http://127.0.0.1:8081/#/users')
            .waitForElementVisible('button[ng-click="openGroupAddModal()"]', 2000)
            .click('button[ng-click="openGroupAddModal()"]')
            .waitForElementVisible('form[name=pgroupAddForm]', 2000)
            .setValue('input[id="id_name"]', 'Group name')
            .setValue('textarea[id="id_description"]', 'This is some group description')
            .waitForElementVisible('button[ng-click="ok()"]', 2000)
            .click('button[ng-click="ok()"]')
            .pause(500)
            .end()
    }
};