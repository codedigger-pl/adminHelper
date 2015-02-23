# namespace
pGroupService = angular.module 'adminHelper.users.services'

###
  Factory PersonGroup

  Angular service for communication with API.
###
pGroupService.factory 'PersonGroup', ['$http', 'Restangular', ($http, Restangular) ->
  new class PersonGroup

    constructor: (@url='api/users/personGroups') ->
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

    post: (new_group) ->
      ###
        Posts new data to API
        :param new_group: {PersonGroup} - post new group to API
      ###
      @base.post(new_group)

    list: () ->
      ###
        Gets all groups from server
      ###
      @base.getList().$object
]