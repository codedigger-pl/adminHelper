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
        console.log 'THEN SECOND'

]