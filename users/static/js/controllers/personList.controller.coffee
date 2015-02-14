# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonList

  Angular controller for person list view.
###
overviewController.controller 'PersonListController', ['$scope', 'Person', ($scope, Person) ->

  class Paginator
    constructor: (itemsPromise) ->
      @currPage = 1
      @items = []
      itemsPromise.then (items) =>
        for item in items
          @items.push(item)
        @itemsCount = @items.length
        stopIndex = Math.min(19, @itemsCount)
        @currVisData = @items[0..stopIndex]

    changePage: () =>
      startIndex = 20*(@currPage-1)
      stopIndex = Math.min(startIndex + 19, @itemsCount)
      @currVisData = @items[startIndex..stopIndex]

  $scope.pager = new Paginator(Person.list(promise=true))

]