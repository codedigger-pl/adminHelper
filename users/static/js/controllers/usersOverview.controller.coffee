# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for main view to person overview part.
###
overviewController.controller 'UsersOverviewController', ['$scope', '$state', '$modal', 'PersonGroup', 'Person', ($scope, $state, $modal, PersonGroup, Person) ->

  # retrieve last registered items
  $scope.persons = Person.get_last_items()
  $scope.groups = PersonGroup.get_last_items()

  # open form allowing add person groups
  $scope.openGroupAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPersonGroup'
      controller: 'PGroupAddModalController'
    instance.result.then \
      () =>
        # refresh last items list
        $scope.groups = PersonGroup.get_last_items()
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
        $scope.persons = Person.get_last_items()
      ,
      () =>
        console.log 'PersonAdd modal closed'

  $scope.showPersonDetails = (id) =>
    $state.go('users.person_detail', { id: id })

]