# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for person add form.
###
overviewController.controller 'PersonAddModalController', ['$scope', '$modalInstance', 'Person', 'djangoForm', ($scope, $modalInstance, Person, djangoForm) ->

  $scope.ok = () ->
    # in template is one form with this name
    form = document.getElementsByName('personAddForm')[0]
    formData = new FormData(form)

    # direct request - left for future tests
    # req = new XMLHttpRequest()
    # req.open('POST', '/api/users/persons/')
    # req.send(formData)

    request = Person.post formData
    request.then \
      () ->
        $modalInstance.close()
      ,
      (response) ->
        if response.status == 400
          djangoForm.setErrors($scope.personAddForm, response.data)

  $scope.cancel = () ->
    $modalInstance.dismiss('cancel')
]