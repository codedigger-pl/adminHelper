overviewController = angular.module 'adminHelper.users.controllers'

overviewController.controller 'PersonAddModalController', ['$scope', '$modalInstance', 'Person', 'djangoForm', ($scope, $modalInstance, Person, djangoForm) ->

  $scope.ok = () ->
    request = Person.post
      rank: $scope.rank
      first_name: $scope.first_name
      last_name: $scope.last_name
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