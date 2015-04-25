modalFactory = angular.module 'adminHelper.users.services'

modalFactory.factory 'sessionFactory', [
  '$modal',
  'Restangular',
  ($modal, Restangular) ->
  new class SessionFactory
    @token = null
    @base = Restangular.all('api/rest-auth')

    @login: (username, password) ->
      resp = @base.customPOST 'login',
        username: username
        password: password
      resp.then (response) ->
        @token = response['key']
        console.log(@token)
]