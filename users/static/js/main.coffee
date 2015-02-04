class Page
  constructor: (@label='', @url='', @stateName='') ->
#
## registering all pages
allPages = []
allPages.push(new Page('Przegląd', '/overview', 'overview'))
allPages.push(new Page('Użytkownicy i pracownicy', '/users/overview', 'users'))
allPages.push(new Page('System alarmowy', '/sswin/overview', 'sswin'))
allPages.push(new Page('System kontroli dostępu', '/acs/overview', 'acs'))
allPages.push(new Page('Klucze', '/keys/overview', 'keys'))

mainApp = angular.module 'adminHelper.mainApp', ['ngRoute', 'ngAnimate', 'ui.bootstrap', 'ui.router', 'restangular']

mainApp.config ['$stateProvider', '$urlRouterProvider', ($stateProvider, $urlRouterProvider) ->

  $urlRouterProvider.otherwise('/users')

  $stateProvider.state 'overview',
    url: '/'
    templateUrl: '/'
    controller: 'UsersController'

  $stateProvider.state 'users',
    url: '/users'
    templateUrl: '/users/overview'
    controller: 'UsersController'

  $stateProvider.state 'sswin',
    url: '/sswin'
    templateUrl: '/sswin/overview'
    controller: 'UsersController'

  $stateProvider.state 'acs',
    url: '/acs'
    templateUrl: '/acs/overview'
    controller: 'UsersController'

  $stateProvider.state 'keys',
    url: '/keys'
    templateUrl: '/keys/overview'
    controller: 'UsersController'
]

# Main controller
mainApp.controller 'MainController', ['$scope', ($scope) ->

  class Page
    constructor: (@label='', @url='', @stateName='') ->

  $scope.tabs = []
  $scope.tabs.push(new Page('Przegląd', '/overview', 'overview'))
  $scope.tabs.push(new Page('Użytkownicy i pracownicy', '/users/overview', 'users'))
  $scope.tabs.push(new Page('System alarmowy', '/sswin/overview', 'sswin'))
  $scope.tabs.push(new Page('System kontroli dostępu', '/acs/overview', 'acs'))
  $scope.tabs.push(new Page('Klucze', '/keys/overview', 'keys'))

]

# Persons list page controller
mainApp.controller 'UsersController', ['$http', '$scope', '$modal', '$log', 'Restangular', ($http, $scope, $modal, $log, Restangular) ->

  # Fetching last 5 persons
  Restangular.allUrl('api/users/persons/?onlyLastItems=5').getList().then (persons) ->
    $scope.persons = persons

  # Fetching last 5 groups
  Restangular.allUrl('api/users/personGroups/?onlyLastItems=5').getList().then (groups) ->
    $scope.groups = groups

  $scope.openGroupAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPersonGroup'
      controller: 'GroupAddController'
    instance.result.then \
      () =>
        $log.info 'THEN CLOSED'
      ,
      () =>
        $log.info 'THEN SECOND'

]

mainApp.controller 'GroupAddController', ['$scope', '$modalInstance', ($scope, $modalInstance) ->

  $scope.ok = () ->
    $modalInstance.close()

  $scope.cancel = () ->
    $modalInstance.dismiss('cancel')
]