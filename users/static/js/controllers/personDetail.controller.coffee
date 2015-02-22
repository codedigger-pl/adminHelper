# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonList

  Angular controller for person list view.
###
overviewController.controller 'PersonDetailController', ['$scope', '$stateParams', 'Person', 'djangoForm', ($scope, $stateParams, Person, djangoForm) ->
  $scope.person = Person.get($stateParams.id)
  if not $scope.person.photo
    $scope.person.photo = '/static/img/unknown_user.jpg'

  $scope.updateCardNumber = () ->
    request = Person.patch($scope.person.id, {card_number: $scope.person.card_number })
    request.then \
      (person) ->
        $scope.person = person
      ,
      (response) ->
        if response.status == 400
          djangoForm.setErrors($scope.cardNumberForm, response.data)

  $scope.updateData = () ->
    request = Person.patch $scope.person.id,
      first_name: $scope.person.first_name
      last_name: $scope.person.last_name
      rank: $scope.person.rank
      group: $scope.person.group
    request.then \
      (person) ->
        $scope.person = person
      ,
      (response) ->
        if response.status == 400
          djangoForm.setErrors($scope.dataForm, response.data)

  $scope.updatePhoto = () ->
    # FormData: only by PUT request?
    console.log('updatePhoto called')
]