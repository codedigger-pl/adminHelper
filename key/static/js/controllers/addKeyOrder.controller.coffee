# namespace
overviewController = angular.module 'adminHelper.key.controllers'

overviewController.controller 'KeyOrderAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  'sessionFactory'
  ($scope, $modalInstance, djangoForm, Restangular, sessionFactory) ->
    ruleBase = Restangular.all('api/keyRules')
    orderBase = Restangular.all('api/keyOrders')

    $scope.ok = ->
      # first request: trying to save new rule
      ruleRequest = ruleBase.post
        person: $scope.KeyRule.person
        key: $scope.KeyRule.key
      ruleRequest.then \
        (rule) ->
          # second request: trying to save new order
          orderRequest = orderBase.post
            rule: rule.id
            user: sessionFactory.user.id
            grant_privilege: $scope.KeyOrder.grant_privilege
          orderRequest.then \
            () ->
              # everything goes fine, closing modal
              $modalInstance.close()
            ,
            (response) ->
              # errors in order form
              if response.status == 400
                djangoForm.setErrors($scope.KeyOrderForm, response.data)
        ,
        (response) ->
          # errors in rule form
          if response.status == 400
            djangoForm.setErrors($scope.KeyRuleForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
