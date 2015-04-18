# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonGroupList

  Angular controller for person group list view.
###
overviewController.controller 'PersonGroupListController', [
  '$scope'
  '$state'
  'Restangular'
  'modalFactory'
  ($scope, $state, Restangular, modalFactory) ->
    base = Restangular.all('api/personGroups')

    $scope.loadData = ->
      $scope.groups = base.getList().$object

    $scope.openGroupAddModal = ->
      instance = modalFactory.openPersonGroupAddModal()
      instance.result.then ->
        $scope.loadData()

    $scope.showPersonGroupDetails = (id) ->
      $state.go('users.personGroup_detail', { id: id })

    $scope.loadData()
]
