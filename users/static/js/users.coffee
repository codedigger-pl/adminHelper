angular.module('adminHelper.usersApp', ['ui.bootstrap'])

angular.module('adminHelper.usersApp').controller 'userOptions', ($scope, $log) ->

angular.module('adminHelper.usersApp').controller 'pageCtr', ($scope, $log) ->
  class Page
    constructor: () ->
      @pageClosed = true

  class OverviewPage extends Page

  class UsersPage extends Page

  class PersonsPage extends Page
    constructor: () ->
      @personsPageClosed = false
      @personPageClosed = true
      @personGroupsPageClosed = true

    closeAllPages: () ->
      @personsPageClosed = true
      @personPageClosed = true
      @personGroupsPageClosed = true

    openPage: (page) ->
      @closeAllPages()
      switch page
        when 'personsPage'
          @personsPageClosed = false
        when 'personPage'
          @personPageClosed = false
        when 'personGroupsPage'
          @personGroupsPageClosed = false

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
    closeAllPages()
    switch page
      when 'overview'
        $scope.overviewPage.pageClosed = false
      when 'users'
        $scope.usersPage.pageClosed = false
      when 'persons'
        $scope.personsPage.pageClosed = false
      when 'sswin'
        $scope.securitySystemsPage.pageClosed = false
      when 'acs'
        $scope.acsPage.pageClosed = false
      when 'keys'
        $scope.keysPage.pageClosed = false

  $scope.openPage 'overview'
