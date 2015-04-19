# namespace
overviewController = angular.module 'adminHelper.alarm.controllers'

overviewController.controller 'AlarmOrderAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  ($scope, $modalInstance, djangoForm, Restangular) ->
    ruleBase = Restangular.all('api/alarmRules')
    orderBase = Restangular.all('api/alarmOrders')

    $scope._ok = ->
      request = base.post
        name: $scope.alarmZone.name
        description: $scope.alarmZone.description
        manager: $scope.alarmZone.manager
      request.then \
        () ->
          $modalInstance.close()
        ,
        (response) ->
          if response.status == 400
            djangoForm.setErrors($scope.alarmZoneForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
