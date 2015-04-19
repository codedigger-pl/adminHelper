# namespace
overviewController = angular.module 'adminHelper.alarm.controllers'

###
  Controller UsersOverview

  Angular controller for main view to alarm overview part.
###
overviewController.controller 'AlarmOverviewController', [
  '$scope'
  '$state'
  'Restangular'
  'alarmModalFactory'
  ($scope, $state, Restangular, alarmModalFactory) ->
    zoneBase = Restangular.all('api/alarmZones')

    $scope.updateZoneData = ->
      $scope.zones = zoneBase.getList().$object

    $scope.openAlarmZoneAddModal = ->
      instance = alarmModalFactory.openAlarmZoneAddModal()
      instance.result.then ->
          $scope.updateZoneData()

    $scope.updateZoneData()

]
