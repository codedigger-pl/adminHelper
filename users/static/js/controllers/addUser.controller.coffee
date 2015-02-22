# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for user add form.
###
overviewController.controller 'UserAddModalController', ['$scope', '$modalInstance', 'User', 'djangoForm', ($scope, $modalInstance, User, djangoForm) ->

  $scope.ok = () ->
    console.log($scope.user)
    request = User.post
      username: $scope.user.username
      first_name: $scope.user.first_name
      last_name: $scope.user.last_name
      rank: $scope.user.rank
      email: $scope.user.email
    request.then \
      () ->
        $modalInstance.close()
      ,
      (response) ->
        if response.status == 400
          djangoForm.setErrors($scope.form, response.data)

  $scope.cancel = () ->
    $modalInstance.dismiss('CANCEL')
]