# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonGroupDetail

  Angular controller for person group detail view.
###
overviewController.controller 'PersonGroupDetailController', [
  '$scope'
  '$stateParams'
  'djangoForm'
  'Restangular'
  ($scope, $stateParams, djangoForm, Restangular) ->
    base = Restangular.all('api/users/personGroups')

    $scope.personGroup = base.get($stateParams.id).$object

    $scope.updateData = ->
      request = $scope.personGroup.patch
        name: $scope.personGroup.name
        description: $scope.personGroup.description
      request.then \
        (group) ->
          $scope.personGroup = group
        ,
        (response) ->
          if response.status == 400
            djangoForm.setErrors($scope.dataForm, response.data)

]
