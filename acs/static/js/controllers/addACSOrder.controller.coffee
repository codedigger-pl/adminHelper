# namespace
overviewController = angular.module 'adminHelper.ACS.controllers'

overviewController.controller 'ACSOrderAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  'sessionFactory'
  ($scope, $modalInstance, djangoForm, Restangular, sessionFactory) ->
    ruleBase = Restangular.all('api/ACSRules')
    orderBase = Restangular.all('api/ACSOrders')

    $scope.ok = ->
      # first request: trying to save new rule
      ruleRequest = ruleBase.post
        person: $scope.ACSRule.person
        zone: $scope.ACSRule.zone
      ruleRequest.then \
        (rule) ->
          # second request: trying to save new order
          orderRequest = orderBase.post
            rule: rule.id
            user: sessionFactory.user.id
            grant_privilege: $scope.ACSOrder.grant_privilege
          orderRequest.then \
            () ->
              # everything goes fine, closing modal
              $modalInstance.close()
            ,
            (response) ->
              # errors in order form
              if response.status == 400
                djangoForm.setErrors($scope.ACSOrderForm, response.data)
        ,
        (response) ->
          # errors in rule form
          if response.status == 400
            djangoForm.setErrors($scope.ACSRuleForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
