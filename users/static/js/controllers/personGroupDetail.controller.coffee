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
    base = Restangular.one('api/users/personGroups', $stateParams.id)
    console.log(base)

    $scope.personGroup = base.get().$object

    $scope.personCount = -1
    base.customGET('person_count').then (resp) ->
      $scope.personCount = resp.count

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
