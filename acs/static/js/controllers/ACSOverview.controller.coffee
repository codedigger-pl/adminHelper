# namespace
overviewController = angular.module 'adminHelper.ACS.controllers'

###
  Controller UsersOverview

  Angular controller for main view to ACS overview part.
###
overviewController.controller 'ACSOverviewController', [
  '$scope'
  '$state'
  'Restangular'
  'ACSModalFactory'
  'sessionFactory'
  ($scope, $state, Restangular, ACSModalFactory, sessionFactory) ->

    sessionFactory.get_logged_user().then \
      (resp) -> sessionFactory.get_user_data(resp.id)
      ,
      () -> $state.go('login')

    zoneBase = Restangular.all('api/ACSZones')
    orderBase = Restangular.all('api/ACSOrders')
    requestBase = Restangular.all('api/ACSRequests')
    ruleBase = Restangular.all('api/ACSRules')

    $scope.updateZoneData = ->
      $scope.zones = zoneBase.getList().$object

    $scope.updateOrderData = ->
      $scope.orders = null
      $scope.orders = orderBase.customGETLIST('', {'nonExecutedOnly': ''}).$object

    $scope.updateRequestData = ->
      $scope.requests = requestBase.getList().$object

    $scope.openACSZoneAddModal = ->
      instance = ACSModalFactory.openACSZoneAddModal()
      instance.result.then ->
          $scope.updateZoneData()

    $scope.openACSOrderAddModal = ->
      instance = ACSModalFactory.openACSOrderAddModal()
      instance.result.then ->
          $scope.updateOrderData()

    $scope.openACSRequestAddModal = ->
      instance = ACSModalFactory.openACSRequestAddModal()
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
