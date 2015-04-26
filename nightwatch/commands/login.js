exports.command = function(username, password, callback) {
    var self = this;
    this
        .maximizeWindow()
        .url('http://127.0.0.1:8081/#/login')
        .waitForElementVisible('input[id="id_username"]', 2000)
        .waitForElementVisible('input[id="id_password"]', 2000)

        .setValue('input[id="id_username"]',username)
        .setValue('input[id="id_password"]', password)
        .click('button[ng-click="ok()"]');

    if (typeof callback === 'function') {
        callback.call(self)
    }
    return this;
};