# namespace
module = angular.module 'adminHelper.users.controllers'

module.controller 'LoginModalController', [
  '$scope'
  '$modalInstance'
  '$state'
  'djangoForm'
  'sessionFactory'
  'Restangular'
  ($scope, $modalInstance, $state, djangoForm, sessionFactory) ->

    $scope.ok = ->
      resp = sessionFactory.login($scope.login.username, $scope.login.password)
      resp.then (response) ->
        sessionFactory.get_user_data(response.id)
        $modalInstance.dismiss('User logged in')
        $state.go('users')

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]

module.controller 'LoginController', [
  '$scope'
  'modalFactory'
  'sessionFactory'
  ($scope, modalFactory, sessionFactory) ->
    modalFactory.openLoginModal()
]
