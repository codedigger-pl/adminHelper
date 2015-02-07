personService = angular.module 'adminHelper.users.services'

personService.factory 'Person', ['$http', 'Restangular', ($http, Restangular) ->
  new class Person
    constructor: (@url='api/users/persons/') ->
      @base = Restangular.all(@url)

    get_last_items: (count=5) ->
      @base.getList({modelType: 'minimal', onlyLastItems: 5}).$object

    post: (new_person) ->
      @base.post(new_person)
]