# namespace
overviewController = angular.module 'adminHelper.key.controllers'

overviewController.controller 'KeyAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  ($scope, $modalInstance, djangoForm, Restangular) ->
    base = Restangular.all('api/keys')

    $scope.ok = ->
      request = base.post
        name: $scope.key.name
        description: $scope.key.description
        manager: $scope.key.manager
      request.then \
        () ->
          $modalInstance.close()
        ,
        (response) ->
          if response.status == 400
            djangoForm.setErrors($scope.KeyForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
