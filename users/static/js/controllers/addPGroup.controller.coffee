overviewController = angular.module 'adminHelper.users.controllers'

overviewController.controller 'PGroupAddModalController', ['$scope', '$modalInstance', ($scope, $modalInstance) ->

  $scope.ok = () ->
    $modalInstance.close()

  $scope.cancel = () ->
    $modalInstance.dismiss('cancel')
]