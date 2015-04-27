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
  'sessionFactory'
  ($scope, $state, Restangular, alarmModalFactory, sessionFactory) ->

    if not sessionFactory.user
      $state.go('login')

    zoneBase = Restangular.all('api/alarmZones')
    orderBase = Restangular.all('api/alarmOrders')
    requestBase = Restangular.all('api/alarmRequests')
    ruleBase = Restangular.all('api/alarmRules')

    $scope.updateZoneData = ->
      $scope.zones = zoneBase.getList().$object

    $scope.updateOrderData = ->
      $scope.orders = null
      $scope.orders = orderBase.customGETLIST('', {'nonExecutedOnly': ''}).$object

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
          user: sessionFactory.user.id
          grant_privilege: request.grant_privilege
        request.remove()
        req.then ->
          $scope.updateOrderData()
          $scope.updateRequestData()

    $scope.deleteRequest = (requestID) ->
      requestBase.get(requestID).then (reqRequest) ->
        ruleBase.get(reqRequest.rule).then (ruleRequest) ->
          ruleRequest.remove()
          reqRequest.remove()
          $scope.updateRequestData()

    $scope.deleteOrder = (orderID) ->
      orderBase.get(orderID).then (orderRequest) ->
        ruleBase.get(orderRequest.rule).then (ruleRequest) ->
          ruleRequest.remove()
          orderRequest.remove()
          $scope.updateOrderData()

    $scope.executeOrder = (orderID) ->
      orderBase.get(orderID).then (orderRequest) ->
        orderRequest.one('execute').post().then (resp) ->
          $scope.updateOrderData()


    $scope.updateZoneData()
    $scope.updateOrderData()
    $scope.updateRequestData()

]
