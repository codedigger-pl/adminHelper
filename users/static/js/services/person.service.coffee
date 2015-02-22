# namespace
personService = angular.module 'adminHelper.users.services'

###
  Factory Person

  Angular service for communication with API.
###
personService.factory 'Person', ['$http', 'Restangular', ($http, Restangular) ->
  new class Person

    constructor: (@url='api/users/persons/') ->
      ###
        Class constructor
        :param url: {str} - API url
      ###
      @base = Restangular.all(@url)

    get_last_items: (count=5) ->
      ###
        Gets last items from database

        :param count: {int} - how many last items retrieve
      ###
      @base.getList({modelType: 'minimal', onlyLastItems: 5}).$object

    post: (new_person) ->
      ###
        Posts new data to API with modified contentType header - needed for multipart POST request.

        :param new_person: {Person-FormData} - post new person to API
      ###
      @base.withHttpConfig({transformRequest: angular.identity}).post(new_person, {}, {'Content-Type': undefined})

    list: (promise=false, lastName='', firstName='') ->
      ###
        Gets all persons from server with filter functionality

        :param promise: {bool} - should we return promise? True as default value.
        :param lastName: {string} - filter for last_name in person
        :param firstName: {string} = filter for first_name in person
        :returns List or promise of list
      ###
      ret = []
      if promise
        ret = @base.getList({last_name: lastName, first_name: firstName})
      else
        ret = @base.getList({last_name: lastName, first_name: firstName}).$object
      ret

    get: (id=1) ->
      ###
        Gets person detail information

        :param id: {int} - person ID
        :returns person detail
      ###
      @base.get(id).$object

    patch: (id, data) ->
      ###
        Update information about person

        :param id: {int} - person ID
        :param data: {{objects}} - person fields dictionary
        :returns API PATCH response
      ###
      @base.get(id).then \
        (person) ->
          person.patch(data)
]