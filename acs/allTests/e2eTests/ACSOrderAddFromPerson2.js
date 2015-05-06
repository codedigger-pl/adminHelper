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
    'opening ACS panel': function (browser) {
        browser
            .useXpath()
            .waitForElementVisible("//span[text()='Dostęp do stref systemu kontroli dostępu']", 2000)
            .click("//span[text()='Dostęp do stref systemu kontroli dostępu']")
            .useCss()
    },
    'adding new rule': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="addToACSZone(ACSZone.id, false)"]', 2000)
            .click('button[ng-click="addToACSZone(ACSZone.id, false)"]')
            .pause(500)
            .end()
    }
};