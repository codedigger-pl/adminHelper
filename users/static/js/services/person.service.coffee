personService = angular.module 'adminHelper.users.services'

personService.factory 'Person', ['$http', 'Restangular', ($http, Restangular) ->
  new class Person
    constructor: (@url='api/users/persons/') ->
      @last_items = []

    get_last_items: (count=5) ->
      Restangular.allUrl(@url+'?modelType=minimal&onlyLastItems='+count).getList().$object
]