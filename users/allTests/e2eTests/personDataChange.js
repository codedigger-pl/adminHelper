module.exports = {
    'finding person': function (browser) {
        browser
            .maximizeWindow()
            .url('http://127.0.0.1:8081/#/users/person_list')
            .waitForElementVisible('tr[ng-click="showPersonDetails(person.id)"]', 2000)
            .click('td')
    },
    'testing person data change form': function (browser) {
        browser
            .waitForElementVisible('button[ng-click="updateData()"]', 2000)
            .waitForElementVisible('input[id="id_first_name"]', 2000)
            .waitForElementVisible('input[id="id_last_name"]', 2000)
            .waitForElementVisible('select[id="id_rank"]', 2000)
            .waitForElementVisible('input[id="id_card_number"]', 2000)
            .waitForElementVisible('select[id="id_group"]', 2000)

            .clearValue('input[id="id_first_name"]')
            .clearValue('input[id="id_last_name"]')
            .clearValue('input[id="id_card_number"]')

            .setValue('input[id="id_first_name"]', 'New first name')
            .setValue('input[id="id_last_name"]', 'New last name')
            .setValue('select[id="id_rank"]', ['pan', browser.Keys.RETURN])
            .setValue('input[id="id_card_number"]', '1111111111111')
            .setValue('select[id="id_group"]', [browser.Keys.DOWN_ARROW, browser.Keys.DOWN_ARROW])
            .click('button[ng-click="updateData()"]')
            .pause(500)
            .end()
    }
};