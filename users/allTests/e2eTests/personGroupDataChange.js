module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'finding person group': function (browser) {
        browser
            .url('http://127.0.0.1:8081/#/users/personGroup_list')
            .waitForElementVisible('tr[ng-click="showPersonGroupDetails(group.id)"]', 2000)
            .click('td')
    },
    'testing person group data change form': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="updateData()"]', 2000)
            .waitForElementVisible('input[id="id_name"]', 2000)
            .waitForElementVisible('textarea[id="id_description"]', 2000)
            .clearValue('input[id="id_name"]')
            .clearValue('textarea[id="id_description"]')
            .setValue('input[id="id_name"]', 'New group name')
            .setValue('textarea[id="id_description"]', 'New group description')
            .click('button[ng-click="updateData()"]')
            .pause(500)
            .end()
    }
};