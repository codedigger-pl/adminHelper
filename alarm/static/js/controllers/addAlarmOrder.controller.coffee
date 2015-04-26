# namespace
overviewController = angular.module 'adminHelper.alarm.controllers'

overviewController.controller 'AlarmOrderAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  'sessionFactory'
  ($scope, $modalInstance, djangoForm, Restangular, sessionFactory) ->
    ruleBase = Restangular.all('api/alarmRules')
    orderBase = Restangular.all('api/alarmOrders')

    $scope.ok = ->
      # first request: trying to save new rule
      ruleRequest = ruleBase.post
        person: $scope.alarmRule.person
        zone: $scope.alarmRule.zone
      ruleRequest.then \
        (rule) ->
          # second request: trying to save new order
          orderRequest = orderBase.post
            rule: rule.id
            user: sessionFactory.user.id
            grant_privilege: $scope.alarmOrder.grant_privilege
          orderRequest.then \
            () ->
              # everything goes fine, closing modal
              $modalInstance.close()
            ,
            (response) ->
              # errors in order form
              if response.status == 400
                djangoForm.setErrors($scope.alarmOrderForm, response.data)
        ,
        (response) ->
          # errors in rule form
          if response.status == 400
            djangoForm.setErrors($scope.alarmRuleForm, response.data)

      # for future use: all in one
#          request = orderBase.post
#        user: $scope.alarmOrder.user
#        grant_privilege: $scope.alarmOrder.grant_privilege
#        rule:
#          person: $scope.alarmRule.person
#          zone: $scope.alarmRule.zone
#      request.then \
#        () ->
#          $modalInstance.close()
#        ,
#        (response) ->
#          if response.status == 400
#            djangoForm.setErrors($scope.alarmRuleForm, response.data)
#            djangoForm.setErrors($scope.alarmOrderForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
