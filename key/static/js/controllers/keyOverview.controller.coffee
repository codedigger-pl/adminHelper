# namespace
overviewController = angular.module 'adminHelper.key.controllers'

###
  Controller UsersOverview

  Angular controller for main view to Key overview part.
###
overviewController.controller 'KeyOverviewController', [
  '$scope'
  '$state'
  'Restangular'
  'KeyModalFactory'
  'sessionFactory'
  ($scope, $state, Restangular, KeyModalFactory, sessionFactory) ->

    sessionFactory.get_logged_user().then \
      (resp) -> sessionFactory.get_user_data(resp.id)
      ,
      () -> $state.go('login')

    zoneBase = Restangular.all('api/keys')
    orderBase = Restangular.all('api/keyOrders')
    requestBase = Restangular.all('api/keyRequests')
    ruleBase = Restangular.all('api/keyRules')

    $scope.updateKeyData = ->
      $scope.keys = zoneBase.getList().$object

    $scope.updateOrderData = ->
      $scope.orders = null
      $scope.orders = orderBase.customGETLIST('', {'nonExecutedOnly': ''}).$object

    $scope.updateRequestData = ->
      $scope.requests = requestBase.getList().$object

    $scope.openKeyAddModal = ->
      instance = KeyModalFactory.openKeyAddModal()
      instance.result.then ->
          $scope.updateKeyData()

    $scope.openKeyOrderAddModal = ->
      instance = KeyModalFactory.openKeyOrderAddModal()
      instance.result.then ->
          $scope.updateOrderData()

    $scope.openKeyRequestAddModal = ->
      instance = KeyModalFactory.openKeyRequestAddModal()
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


    $scope.updateKeyData()
    $scope.updateOrderData()
    $scope.updateRequestData()

]
