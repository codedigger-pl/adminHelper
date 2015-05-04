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
    'opening alarm panel': function (browser) {
        browser
            .useXpath()
            .waitForElementVisible("//span[text()='Dostęp do stref systemu alarmowego']", 2000)
            .click("//span[text()='Dostęp do stref systemu alarmowego']")
            .useCss()
    },
    'adding new rules': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="addToAlarmZone(alarmZone.id, false)"]', 2000)
            .click('button[ng-click="addToAlarmZone(alarmZone.id, false)"]')
            .pause(500)
            .end()
    }
};