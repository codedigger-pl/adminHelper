# namespace
overviewController = angular.module 'adminHelper.ACS.controllers'

overviewController.controller 'ACSRequestAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  'sessionFactory'
  ($scope, $modalInstance, djangoForm, Restangular, sessionFactory) ->
    ruleBase = Restangular.all('api/ACSRules')
    requestBase = Restangular.all('api/ACSRequests')

    $scope.ok = ->
      # first request: trying to save new rule
      ruleRequest = ruleBase.post
        person: $scope.ACSRule.person
        zone: $scope.ACSRule.zone
      ruleRequest.then \
        (rule) ->
          # second request: trying to save new request
          requestRequest = requestBase.post
            rule: rule.id
            user: sessionFactory.user.id
            grant_privilege: $scope.ACSRequest.grant_privilege
          requestRequest.then \
            () ->
              # everything goes fine, closing modal
              $modalInstance.close()
            ,
            (response) ->
              # errors in order form
              if response.status == 400
                djangoForm.setErrors($scope.ACSRequestForm, response.data)
        ,
        (response) ->
          # errors in rule form
          if response.status == 400
            djangoForm.setErrors($scope.ACSRuleForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
