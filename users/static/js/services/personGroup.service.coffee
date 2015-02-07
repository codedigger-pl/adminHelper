pGroupService = angular.module 'adminHelper.users.services'

pGroupService.factory 'PersonGroup', ['$http', 'Restangular', ($http, Restangular) ->
  new class PersonGroup
    constructor: (@url='api/users/personGroups/') ->
      @base = Restangular.all(@url)

    get_last_items: (count=5) ->
      @base.getList({modelType: 'minimal', onlyLastItems: 5}).$object

    post: (new_group) ->
      @base.post(new_group)
]