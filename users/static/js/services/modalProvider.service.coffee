modalProvider = angular.module 'adminHelper.users.services'

modalProvider.service 'modalProvider', ['$modal', ($modal) ->

  @openPersonGroupAddModal = ->
    $modal.open
      templateUrl: '/users/addPersonGroup'
      controller: 'PGroupAddModalController'

]