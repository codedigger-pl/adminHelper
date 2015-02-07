pGroupService = angular.module 'adminHelper.users.services'

pGroupService.factory 'PersonGroup', ['$http', 'Restangular', ($http, Restangular) ->
  new class PersonGroup
    constructor: (@url='api/users/personGroups/') ->
      @last_items = []
      @base = Restangular.all(@url)

    get_last_items: (count=5) ->
      Restangular.allUrl(@url+'?modelType=minimal&onlyLastItems='+count).getList().$object

    post: (new_group) ->
      @base.post(new_group)
]