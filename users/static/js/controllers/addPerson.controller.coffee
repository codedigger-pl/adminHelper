# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for person add form.
###
overviewController.controller 'PersonAddModalController', ['$scope', '$modalInstance', 'Person', 'djangoForm', ($scope, $modalInstance, Person, djangoForm) ->

  $scope.ok = () ->
    console.log('photo: '+$scope.photo)
    console.log('last_name: '+$scope.last_name)
    request = Person.post
      rank: $scope.rank
      first_name: $scope.first_name
      last_name: $scope.last_name
      photo: $scope.photo
      card_number: $scope.card_number
      group: $scope.group
    request.then \
      () ->
        $modalInstance.close()
      ,
      (response) ->
        if response.status == 400
          djangoForm.setErrors($scope.form, response.data)

  $scope.cancel = () ->
    $modalInstance.dismiss('cancel')
]