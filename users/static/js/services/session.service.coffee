module = angular.module 'adminHelper.users.services'

module.factory 'sessionFactory', [
  '$http'
  'Restangular'
  ($http, Restangular) ->

    new class SessionFactory

      constructor: ->
        @user = null
        $http.defaults.xsrfCookieName = 'csrftoken'
        $http.defaults.xsrfHeaderName = 'X-CSRFToken'
        @all_base = Restangular.all('api/users')
        @login_base = Restangular.all('api/users/login')

      login: (username, password) ->
        @login_base.post
          username: username
          password: password

      get_user_data: (id) ->
        @user = @all_base.get(id).$object

      get_logged_user: ->
        @all_base.get('logged_user')
]