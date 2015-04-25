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
    orderBase = Restangular.all('api/alarmOrders')
    requestBase = Restangular.all('api/alarmRequests')
    ruleBase = Restangular.all('api/alarmRules')

    $scope.updateZoneData = ->
      $scope.zones = zoneBase.getList().$object

    $scope.updateOrderData = ->
      $scope.orders = orderBase.getList().$object

    $scope.updateRequestData = ->
      $scope.requests = requestBase.getList().$object

    $scope.openAlarmZoneAddModal = ->
      instance = alarmModalFactory.openAlarmZoneAddModal()
      instance.result.then ->
          $scope.updateZoneData()

    $scope.openAlarmOrderAddModal = ->
      instance = alarmModalFactory.openAlarmOrderAddModal()
      instance.result.then ->
          $scope.updateOrderData()

    $scope.openAlarmRequestAddModal = ->
      instance = alarmModalFactory.openAlarmRequestAddModal()
      instance.result.then ->
          $scope.updateRequestData()

    $scope.acceptRequest = (requestID) ->
      requestBase.get(requestID).then (request) ->
        req = orderBase.post
          rule: request.rule
          user: 1
          grant_privilege: request.grant_privilege
        request.remove()
        req.then ->
          $scope.updateOrderData()
          $scope.updateRequestData()

    $scope.updateZoneData()
    $scope.updateOrderData()
    $scope.updateRequestData()

]
