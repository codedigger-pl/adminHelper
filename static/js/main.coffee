#class Page
#  constructor: (@label='', @url='', @stateName='') ->
#
## registering all pages
#allPages = []
#allPages.push(new Page('Przegląd', '/overview', 'overview'))
#allPages.push(new Page('Użytkownicy i pracownicy', '/users/overview', 'users'))
#allPages.push(new Page('System alarmowy', '/sswin/overview', 'sswin'))
#allPages.push(new Page('System kontroli dostępu', '/acs/overview', 'acs'))
#allPages.push(new Page('Klucze', '/keys/overview', 'keys'))

mainApp = angular.module 'adminHelper', [
  'ngRoute'
  'ngAnimate'
  'ui.bootstrap'
  'ui.router'
  'restangular'
  'adminHelper.users'
  'adminHelper.alarm'
  'adminHelper.ACS'
  'adminHelper.key']

mainApp.config [
  '$stateProvider'
  '$urlRouterProvider'
  ($stateProvider, $urlRouterProvider) ->
    $urlRouterProvider.otherwise('/login')

    $stateProvider.state 'overview',
      url: '/'
      templateUrl: '/'
      controller: 'UsersOverviewController'

    $stateProvider.state 'login',
      url: '/login'
      templateUrl: '/users/login_view'
      controller: 'LoginController'

    $stateProvider.state 'users',
      url: '/users'
      templateUrl: '/users/overview'
      controller: 'UsersOverviewController'

    $stateProvider.state 'users.person_list',
      url: '/person_list'
      templateUrl: '/users/person_list'
      controller: 'PersonListController'

    $stateProvider.state 'users.person_detail',
      url: '^/person_detail/{id:int}'
      templateUrl: '/users/person_detail'
      controller: 'PersonDetailController'

    $stateProvider.state 'users.personGroup_list',
      url: '/personGroup_list'
      templateUrl: '/users/personGroup_list'
      controller: 'PersonGroupListController'

    $stateProvider.state 'users.personGroup_detail',
      url: '^/personGroup_detail/{id:int}'
      templateUrl: '/users/personGroup_detail'
      controller: 'PersonGroupDetailController'

    $stateProvider.state 'alarm',
      url: '/alarm'
      templateUrl: '/alarm/overview'
      controller: 'AlarmOverviewController'

    $stateProvider.state 'acs',
      url: '/acs'
      templateUrl: '/acs/overview'
      controller: 'ACSOverviewController'

    $stateProvider.state 'key',
      url: '/keys'
      templateUrl: '/key/overview'
      controller: 'KeyOverviewController'
]

# Main controller
mainApp.controller 'MainController', ['$scope', ($scope) ->

  class Page
    constructor: (@label='', @url='', @stateName='') ->

  $scope.tabs = []
  $scope.tabs.push(new Page('Przegląd', '/overview', 'overview'))
  $scope.tabs.push(new Page('Użytkownicy i pracownicy', '/users/overview', 'users'))
  $scope.tabs.push(new Page('System alarmowy', '/alarm/overview', 'alarm'))
  $scope.tabs.push(new Page('System kontroli dostępu', '/acs/overview', 'acs'))
  $scope.tabs.push(new Page('Klucze', '/keys/overview', 'key'))

]