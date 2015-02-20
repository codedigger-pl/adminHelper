# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonList

  Angular controller for person list view.
###
overviewController.controller 'PersonDetailController', ['$scope', '$stateParams', 'Person', 'djangoForm', ($scope, $stateParams, Person, djangoForm) ->
  $scope.person = Person.get($stateParams.id)

  $scope.updateCardNumber = () ->
    request = Person.patch($scope.person.id, {card_number: $scope.person.card_number })
    request.then \
      (person) ->
        $scope.person = person
      ,
      (response) ->
        if response.status == 400
          djangoForm.setErrors($scope.cardNumberForm, response.data)
]