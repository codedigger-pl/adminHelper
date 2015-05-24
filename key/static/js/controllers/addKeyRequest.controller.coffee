# namespace
overviewController = angular.module 'adminHelper.key.controllers'

overviewController.controller 'KeyRequestAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  'sessionFactory'
  ($scope, $modalInstance, djangoForm, Restangular, sessionFactory) ->
    ruleBase = Restangular.all('api/keyRules')
    requestBase = Restangular.all('api/keyRequests')

    $scope.ok = ->
      # first request: trying to save new rule
      ruleRequest = ruleBase.post
        person: $scope.KeyRule.person
        key: $scope.KeyRule.key
      ruleRequest.then \
        (rule) ->
          # second request: trying to save new request
          requestRequest = requestBase.post
            rule: rule.id
            user: sessionFactory.user.id
            grant_privilege: $scope.KeyRequest.grant_privilege
          requestRequest.then \
            () ->
              # everything goes fine, closing modal
              $modalInstance.close()
            ,
            (response) ->
              # errors in order form
              if response.status == 400
                djangoForm.setErrors($scope.KeyRequestForm, response.data)
        ,
        (response) ->
          # errors in rule form
          if response.status == 400
            djangoForm.setErrors($scope.KeyRuleForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
