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

mainApp = angular.module 'adminHelper', ['ngRoute', 'ngAnimate', 'ui.bootstrap', 'ui.router', 'restangular', 'adminHelper.users']

mainApp.config ['$stateProvider', '$urlRouterProvider', ($stateProvider, $urlRouterProvider) ->

  $urlRouterProvider.otherwise('/users')

  $stateProvider.state 'overview',
    url: '/'
    templateUrl: '/'
    controller: 'UsersOverviewController'

  $stateProvider.state 'users',
    url: '/users'
    templateUrl: '/users/overview'
    controller: 'UsersOverviewController'

  $stateProvider.state 'sswin',
    url: '/sswin'
    templateUrl: '/sswin/overview'
    controller: 'UsersOverviewController'

  $stateProvider.state 'acs',
    url: '/acs'
    templateUrl: '/acs/overview'
    controller: 'UsersOverviewController'

  $stateProvider.state 'keys',
    url: '/keys'
    templateUrl: '/keys/overview'
    controller: 'UsersOverviewController'
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