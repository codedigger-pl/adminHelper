# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for main view to person overview part.
###
overviewController.controller 'UsersOverviewController', ['$scope', '$state', '$modal', 'Restangular', ($scope, $state, $modal, Restangular) ->

  $scope.groups = []
  $scope.groupsCount = -1
  $scope.persons = []
  $scope.personsCount = -1

  base_personGroup = Restangular.all('api/users/personGroups')
  base_person = Restangular.all('api/users/persons')

  refreshLastPersonGroups = () ->
    $scope.groups = base_personGroup.getList({modelType: 'minimal', onlyLastItems: 5}).$object

  refreshLastPersons = () ->
    $scope.persons = base_person.getList({modelType: 'minimal', onlyLastItems: 5}).$object

  refreshPersonGroupsCount = () ->
    base_personGroup.get('count').then (count) =>
      $scope.groupsCount = count.count

  refreshPersonsCount = () ->
    base_person.get('count').then (count) =>
      $scope.personsCount = count.count

  $scope.refreshPersonGroupsData = () ->
    refreshLastPersonGroups()
    refreshPersonGroupsCount()

  $scope.refreshPersonsData = () ->
    refreshLastPersons()
    refreshPersonsCount()

  $scope.refreshPageData = () ->
    $scope.refreshPersonGroupsData()
    $scope.refreshPersonsData()

  $scope.refreshPageData()

  # open form allowing add person groups
  $scope.openGroupAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPersonGroup'
      controller: 'PGroupAddModalController'
    instance.result.then \
      () =>
        # refresh last items list
        $scope.refreshPersonGroupsData()
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
        $scope.refreshPersonsData()
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
