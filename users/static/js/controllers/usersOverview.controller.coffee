# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for main view to person overview part.
###
overviewController.controller 'UsersOverviewController', [
  '$scope'
  '$state'
  'Restangular'
  'modalFactory'
  ($scope, $state, Restangular, modalFactory) ->

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
    $scope.openGroupAddModal = ->
      instance = modalFactory.openPersonGroupAddModal()
      instance.result.then ->
          $scope.groups.refreshData()

    # open form allowing add persons
    $scope.openPersonAddModal = ->
      instance = modalFactory.openPersonAddModal()
      instance.result.then ->
          $scope.persons.refreshData()

    # open form allowing add users
    $scope.openUserAddModal = ->
      instance = modalFactory.openUserAddModal()
      instance.result.then ->
          $scope.users.refreshData()

    # going to another views
    $scope.showPersonDetails = (id) =>
      $state.go('users.person_detail', { id: id })

    $scope.showPersonGroupDetails = (id) =>
      $state.go('users.personGroup_detail', { id: id })
]
