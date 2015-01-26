mainApp = angular.module 'adminHelper.mainApp', ['ngRoute', 'ngAnimate', 'ui.bootstrap']
mainApp.config ['$routeProvider', '$locationProvider', ($routeProvider, $locationProvider) ->

  # route settings for persons list page
  $routeProvider.when '/persons/'
    templateUrl: '/users/',
    controller: 'PersonsCtrl',
    controllerAs: 'persons'

  # route settings fot person detail page
  $routeProvider.when '/persons/:personID'
    templateUrl: '/persons',
    controller: 'PersonCtrl',
    controllerAs: 'person'

  # route settings fot person groups settings
  $routeProvider.when '/personGroups'
    templateUrl: 'book.html',
    controller: 'PersonGroupsCtrl',
    controllerAs: 'personGroups'

  $locationProvider.html5Mode true
]

# Main controller
mainApp.controller 'MainCtrl', ['$route', '$routeParams', '$location', ($route, $routeParams, $location) ->
  @$route = $route
  @$location = $location
  @$routeParams = $routeParams
]

# Persons list page controller
mainApp.controller 'PersonsCtrl', ['$routeParams', ($routeParams) ->
  @name = 'PersonsCtrl'
  @params = $routeParams
]

# Person page controller
mainApp.controller 'PersonCtrl', ['$routeParams', ($routeParams) ->
  @name = 'PersonCtrl'
  @params = $routeParams
]

# Person groups controller
mainApp.controller 'PersonGroupsCtrl' ,['$routeParams', ($routeParams) ->
  @name = 'PersonGroupsCtr'
  @params = $routeParams
]
