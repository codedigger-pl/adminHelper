module.exports = {
    'login to system': function (browser) {
        browser
            .login('test_user', 'test_user')
    },
    'finding person': function (browser) {
        browser
            .url('http://127.0.0.1:8081/#/users/person_list')
            .waitForElementVisible('tr[ng-click="showPersonDetails(person.id)"]', 2000)
            .click('td')
    },
    'opening key panel': function (browser) {
        browser
            .useXpath()
            .waitForElementVisible("//span[text()='Dostęp do kluczy']", 2000)
            .click("//span[text()='Dostęp do kluczy']")
            .useCss()
    },
    'adding new rules': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="addToKey(key.id, true)"]', 2000)
            .click('button[ng-click="addToKey(key.id, true)"]')
            .pause(500)
            .end()
    }
};