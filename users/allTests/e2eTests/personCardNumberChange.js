module.exports = {
    'finding person': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/users/person_list')
            .waitForElementVisible('tr[ng-click="showPersonDetails(person.id)"]', 2000)
            .click('td')
    },
    'testing person card number change form': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="updateCardNumber()"]', 2000)
            .waitForElementVisible('input[id="id_card_number"]', 2000)
            .clearValue('input[id="id_card_number"]')
            .setValue('input[id="id_card_number"]', '2222222222')
            .click('button[ng-click="updateCardNumber()"]')
            .pause(500)
            .end()
    }
};