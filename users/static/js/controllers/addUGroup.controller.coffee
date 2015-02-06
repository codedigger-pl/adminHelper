overviewController = angular.module 'adminHelper.users.controllers'

overviewController.controller 'GroupAddModalController', ['$scope', '$modalInstance', ($scope, $modalInstance) ->

  $scope.ok = () ->
    $modalInstance.close()

  $scope.cancel = () ->
    $modalInstance.dismiss('cancel')
]