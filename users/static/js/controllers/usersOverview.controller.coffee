overviewController = angular.module 'adminHelper.users.controllers'

overviewController.controller 'UsersOverviewController', ['$scope', '$modal', 'PersonGroup', 'Person', ($scope, $modal, PersonGroup, Person) ->

  $scope.persons = Person.get_last_items()
  $scope.groups = PersonGroup.get_last_items()

  $scope.openGroupAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPersonGroup'
      controller: 'PGroupAddModalController'
    instance.result.then \
      () =>
        $scope.groups = PersonGroup.get_last_items()
      ,
      () =>
        console.log 'GroupAdd modal closed'

  $scope.openPersonAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPerson'
      controller: 'PersonAddModalController'
    instance.result.then \
      () =>
        $scope.persons = Person.get_last_items()
      ,
      () =>
        console.log 'PersonAdd modal closed'

]