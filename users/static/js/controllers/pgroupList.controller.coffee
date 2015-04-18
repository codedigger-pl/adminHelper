# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonGroupList

  Angular controller for person group list view.
###
overviewController.controller 'PersonGroupListController', [
  '$scope'
  'Restangular'
  'modalFactory'
  ($scope, Restangular, modalFactory) ->
    base = Restangular.all('api/users/personGroups')

    $scope.loadData = ->
      $scope.groups = base.getList().$object

    $scope.openGroupAddModal = ->
      instance = modalFactory.openPersonGroupAddModal()
      instance.result.then ->
        $scope.loadData()

    $scope.loadData()
]
