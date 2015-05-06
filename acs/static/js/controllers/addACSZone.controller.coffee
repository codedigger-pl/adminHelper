# namespace
overviewController = angular.module 'adminHelper.ACS.controllers'

overviewController.controller 'ACSZoneAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  ($scope, $modalInstance, djangoForm, Restangular) ->
    base = Restangular.all('api/ACSZones')

    $scope.ok = ->
      request = base.post
        name: $scope.ACSZone.name
        description: $scope.ACSZone.description
        manager: $scope.ACSZone.manager
      request.then \
        () ->
          $modalInstance.close()
        ,
        (response) ->
          if response.status == 400
            djangoForm.setErrors($scope.ACSZoneForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
