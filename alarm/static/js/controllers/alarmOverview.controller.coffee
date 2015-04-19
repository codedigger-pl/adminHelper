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

    $scope.zones = []

    $scope.updateZoneData = ->
      $scope.zones = []
      zoneBase.getList().then (zones) ->
        for zone in zones
          Restangular.one('api/users', zone.manager).get().then (manager) ->
            zone.manager = manager.last_name + ' ' + manager.first_name
          $scope.zones.push(zone)

    $scope.openAlarmZoneAddModal = ->
      instance = alarmModalFactory.openAlarmZoneAddModal()
      instance.result.then ->
          $scope.updateZoneData()

    $scope.updateZoneData()

]
