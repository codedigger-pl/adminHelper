module.exports = {
    'testing person group add form': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/users')
            .waitForElementVisible('button[ng-click="openGroupAddModal()"]', 5000)
            .click('button[ng-click="openGroupAddModal()"]')
            .waitForElementVisible('form[name=pgroupAddForm]', 5000)
            .setValue('input[id="id_name"]', 'Group name')
            .setValue('textarea[id="id_description"]', 'This is some group description')
            .waitForElementVisible('button[ng-click="ok()"]', 5000)
            .click('button[ng-click="ok()"]')
            .pause(2000)
            .end()
    }
};