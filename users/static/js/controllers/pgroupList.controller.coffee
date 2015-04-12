# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonGroupList

  Angular controller for person group list view.
###
overviewController.controller 'PersonGroupListController', ['$scope', 'Restangular', ($scope, Restangular) ->
  base = Restangular.all('api/users/personGroups')

  $scope.groups = base.getList().$object
]
