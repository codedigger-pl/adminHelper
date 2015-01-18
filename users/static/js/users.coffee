angular.module('adminHelper.usersApp', ['ui.bootstrap'])

angular.module('adminHelper.usersApp').controller 'userOptions', ($scope, $log) ->

angular.module('adminHelper.usersApp').controller 'pageCtr', ($scope, $log) ->
  class Page
    constructor: () ->
      @pageClosed = true

  class OverviewPage extends Page

  class UsersPage extends Page

  class PersonsPage extends Page

  class SecuritySystemsPage extends Page

  class ACSPage extends Page

  class KeysPage extends Page

  $scope.overviewPage = new OverviewPage()
  $scope.usersPage = new UsersPage()
  $scope.personsPage = new PersonsPage()
  $scope.securitySystemsPage = new SecuritySystemsPage()
  $scope.acsPage = new ACSPage()
  $scope.keysPage = new KeysPage()

  closeAllPages = ->
    $scope.overviewPage.pageClosed = true
    $scope.usersPage.pageClosed = true
    $scope.personsPage.pageClosed = true
    $scope.securitySystemsPage.pageClosed = true
    $scope.acsPage.pageClosed = true
    $scope.keysPage.pageClosed = true

  $scope.openPage = (page) ->
    switch page
      when 'overview'
        closeAllPages()
        $scope.overviewPage.pageClosed = false
      when 'users'
        closeAllPages()
        $scope.usersPage.pageClosed = false
      when 'persons'
        closeAllPages()
        $scope.personsPage.pageClosed = false
      when 'sswin'
        closeAllPages()
        $scope.securitySystemsPage.pageClosed = false
      when 'acs'
        closeAllPages()
        $scope.acsPage.pageClosed = false
      when 'keys'
        closeAllPages()
        $scope.keysPage.pageClosed = false

  $scope.openPage 'overview'
