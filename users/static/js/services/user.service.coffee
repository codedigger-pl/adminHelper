# namespace
personService = angular.module 'adminHelper.users.services'

###
  Factory User

  Angular service for communication with API.
###
personService.factory 'User', ['$http', 'Restangular', ($http, Restangular) ->
  new class User

    constructor: (@url='api/users/users') ->
      ###
        Class constructor
        :param url: {str} - API url
      ###
      @base = Restangular.all(@url)

    post: (new_user) ->
      ###
        Posts new data to API
      ###
      @base.post(new_user)

    list: (promise=false, lastName='', firstName='') ->
      ###
        Gets all users from server
      ###
      @base.getList({last_name: lastName, first_name: firstName}).$object

    get: (id=1) ->
      ###
        Gets user detail information

        :param id: {int} - user ID
        :returns user detail
      ###
      @base.get(id).$object

    patch: (id, data) ->
      ###
        Update information about user

        :param id: {int} - user ID
        :param data: {{objects}} - user fields dictionary
        :returns API PATCH response
      ###
      @base.get(id).then \
        (user) ->
          user.patch(data)
]
