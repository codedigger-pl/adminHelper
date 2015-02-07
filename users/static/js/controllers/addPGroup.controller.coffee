overviewController = angular.module 'adminHelper.users.controllers'

overviewController.controller 'PGroupAddModalController', ['$scope', '$modalInstance', 'PersonGroup', 'djangoForm', ($scope, $modalInstance, PersonGroup, djangoForm) ->

  $scope.ok = () ->
    request = PersonGroup.post
      name: $scope.name
      description: $scope.description
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