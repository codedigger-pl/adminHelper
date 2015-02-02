class Page
  constructor: (@label='', @url='', @templateUrl='', @controller='', @controllerAs='') ->

# registering all pages
allPages = []
allPages.push(new Page('Przegląd', '/overview', '/overview', 'OverviewCtrl', 'overview'))
allPages.push(new Page('Użytkownicy i pracownicy', '/users/overview', '/users/overview', 'UsersCtrl', 'users'))
allPages.push(new Page('System alarmowy', '/sswin/overview', '/sswin/overview', 'SSWiNCtrl', 'sswin'))
allPages.push(new Page('System kontroli dostępu', '/acs/overview', '/acs/overview', 'ACSCtrl', 'acs'))
allPages.push(new Page('Klucze', '/keys/overview', '/acs/overview', 'KeysCtrl', 'keys'))

mainApp = angular.module 'adminHelper.mainApp', ['ngRoute', 'ngAnimate', 'ui.bootstrap']
mainApp.config ['$routeProvider', '$locationProvider', ($routeProvider, $locationProvider) ->

  # setting route for registered pages
  for page in allPages
    $routeProvider.when page.url,
      templateUrl: page.templateUrl
      controller: page.controller
      controllerAs: page.controllerAs

  $locationProvider.html5Mode true
]

# Main controller
mainApp.controller 'MainCtrl', ['$route', '$routeParams', '$location', '$scope', ($route, $routeParams, $location, $scope) ->
  @$route = $route
  @$location = $location
  @$routeParams = $routeParams

  $scope.tabs = []
  for tab in allPages
    $scope.tabs.push
      url: tab.url
      label: tab.label

]

# Persons list page controller
mainApp.controller 'UsersCtrl', ['$routeParams', '$http', '$scope', '$modal', '$log', ($routeParams, $http, $scope, $modal, $log) ->

  class PersonList
    constructor: (@url='/api/users/persons/?onlyLastItems=5&modelType=minimal') ->
      @persons = []

    get_from_server: ->
      $http.get(@url).then \
        (result) =>
          @persons = []
          angular.forEach result.data, (item) =>
            @persons.push item
        ,
        =>
          alert 'Problem with downloading Persons from server'

  class PersonGroupList
    constructor: (@url='/api/users/personGroups/?onlyLastItems=5') ->
      @groups = []

    get_from_server: ->
      $http.get(@url).then \
        (result) =>
          @groups = []
          angular.forEach result.data, (item) =>
            @groups.push item
        ,
        =>
          alert 'Problem with downloading Persons from server'


  @name = 'UsersCtrl'
  @params = $routeParams

  $scope.personList = new PersonList()
  $scope.personList.get_from_server()

  $scope.personGroupList = new PersonGroupList()
  $scope.personGroupList.get_from_server()

  $scope.openGroupAddModal = () ->
    instance = $modal.open
      templateUrl: '/users/addPersonGroup'
      controller: 'GroupAddCtrl'
    instance.result.then \
      () =>
        $log.info 'THEN CLOSED'
      ,
      () =>
        $log.info 'THEN SECOND'

]

mainApp.controller 'GroupAddCtrl', ['$scope', '$modalInstance', ($scope, $modalInstance) ->

  $scope.ok = () ->
    $modalInstance.close()

  $scope.cancel = () ->
    $modalInstance.dismiss('cancel')
]