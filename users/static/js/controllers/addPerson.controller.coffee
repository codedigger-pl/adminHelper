# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for person add form.
###
overviewController.controller 'PersonAddModalController', [
  '$scope'
  '$modalInstance'
  'djangoForm'
  'Restangular'
  ($scope, $modalInstance, djangoForm, Restangular) ->
    base = Restangular.all('api/persons')

    $scope.ok = ->
      # in template is one form with this name
      form = document.getElementsByName('personAddForm')[0]
      formData = new FormData(form)

      # direct request - left for future tests
      # req = new XMLHttpRequest()
      # req.open('POST', '/api/users/persons/')
      # req.send(formData)

      request = base.withHttpConfig({transformRequest: angular.identity}).post(formData, {}, {'Content-Type': undefined})
      request.then \
        () ->
          $modalInstance.close()
        ,
        (response) ->
          if response.status == 400
            djangoForm.setErrors($scope.personAddForm, response.data)

    $scope.cancel = ->
      $modalInstance.dismiss('cancel')
]
