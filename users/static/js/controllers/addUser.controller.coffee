# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller UsersOverview

  Angular controller for user add form.
###
overviewController.controller 'UserAddModalController', ['$scope', '$modalInstance', 'djangoForm', 'Restangular', ($scope, $modalInstance, djangoForm, Restangular) ->
  base = Restangular.all('api/users/users')

  $scope.ok = () ->
    console.log($scope.user)
    request = base.post
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
