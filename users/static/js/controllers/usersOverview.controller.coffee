# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for main view to person overview part.
###
overviewController.controller 'UsersOverviewController', ['$scope', '$state', '$modal', 'Restangular', ($scope, $state, $modal, Restangular) ->

  class ItemInfo
    constructor: (url) ->
      @base = Restangular.all(url)
      @items = []
      @itemsCount = -1
      @lastRegistered = ''

    getItems: ->
      @items = @base.getList({modelType: 'minimal', onlyLastItems: 5}).$object

    getItemsCount: ->
      @base.get('count').then (count) =>
        @itemsCount = count.count

    getLastRegistered: () ->
      @base.get('last_registered').then (name) =>
        @lastRegistered = name.name

    refreshData: ->
      @getItems()
      @getItemsCount()
      @getLastRegistered()

  class UserItemInfo extends ItemInfo
    getItems: ->
      @items = @base.getList().$object

  $scope.groups = new ItemInfo('api/users/personGroups')
  $scope.persons = new ItemInfo('api/users/persons')
  $scope.users = new UserItemInfo('api/users/users')

  $scope.groups.refreshData()
  $scope.persons.refreshData()
  $scope.users.refreshData()

  # open form allowing add person groups
  $scope.openGroupAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPersonGroup'
      controller: 'PGroupAddModalController'
    instance.result.then \
      () =>
        # refresh last items list
        $scope.groups.refreshData()
      ,
      () =>
        console.log 'GroupAdd modal closed'

  # open form allowing add perons
  $scope.openPersonAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPerson'
      controller: 'PersonAddModalController'
    instance.result.then \
      () =>
        # refresh last items list
        $scope.persons.refreshData()
      ,
      () =>
        console.log 'PersonAdd modal closed'

  # open form allowing add users
  $scope.openUserAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addUser'
      controller: 'UserAddModalController'
    instance.result.then \
      () =>
        # refresh last items list
        $scope.users = Person.get_last_items()
      ,
      () =>
        console.log 'PersonAdd modal closed'

  $scope.showPersonDetails = (id) =>
    $state.go('users.person_detail', { id: id })
]
