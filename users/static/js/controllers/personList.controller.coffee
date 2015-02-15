# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonList

  Angular controller for person list view.
###
overviewController.controller 'PersonListController', ['$scope', '$state', 'Person', ($scope, $state, Person) ->

  class Paginator
    constructor: () ->
      @currPage = 1
      @items = []
      @itemsCount = 0
      @currVisItems = []
      @lastNameFilter=''
      @firstNameFilter=''
#      Person.list(promise=true).then (items) =>
#        for item in items
#          @items.push(item)
#        @itemsCount = @items.length
#        stopIndex = Math.min(19, @itemsCount)
#        @currVisData = @items[0..stopIndex]

    changePage: () =>
      startIndex = 20*(@currPage-1)
      stopIndex = Math.min(startIndex + 19, @itemsCount)
      @currVisItems = @items[startIndex..stopIndex]

    newSearch: () =>

    loadData: () =>
      @currVisItems = []
      @items = []
      Person.list(promise=true, lastName=@lastNameFilter, firstName=@firstNameFilter).then (items) =>
        for item in items
          @items.push(item)
        @itemsCount = @items.length
        stopIndex = Math.min(19, @itemsCount)
        @currVisItems = @items[0..stopIndex]

  $scope.showPersonDetails = (id) =>
    $state.go('users.person_detail', { id: id })

  $scope.pager = new Paginator()
  $scope.pager.loadData()

]