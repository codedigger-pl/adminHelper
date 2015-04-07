# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonGroupList

  Angular controller for person group list view.
###
overviewController.controller 'PersonGroupListController', ['$scope', 'PersonGroup', ($scope, PersonGroup) ->
  $scope.groups = PersonGroup.list()
]
