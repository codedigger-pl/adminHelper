# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonList

  Angular controller for person list view.
###
overviewController.controller 'PersonDetailController', ['$scope', '$stateParams', 'Person', ($scope, $stateParams, Person) ->
  console.log($stateParams.id)
]