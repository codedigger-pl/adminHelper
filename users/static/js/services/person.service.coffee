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
        Posts new data to API
        :param new_person: {Person} - post new person to API
      ###
      @base.post(new_person)

    list: () ->
      ###
        Gets all persons from server
      ###
      @base.getList().$object
]