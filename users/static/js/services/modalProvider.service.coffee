modalFactory = angular.module 'adminHelper.users.services'

modalFactory.factory 'modalFactory', ['$modal', ($modal) ->
  new class ModalFactory

    openPersonGroupAddModal: ->
      $modal.open
        templateUrl: '/users/addPersonGroup'
        controller: 'PGroupAddModalController'

    openPersonAddModal: ->
      $modal.open
        templateUrl: '/users/addPerson'
        controller: 'PersonAddModalController'

    openUserAddModal: ->
      $modal.open
        templateUrl: '/users/addUser'
        controller: 'UserAddModalController'

    openLoginModal: ->
      $modal.open
        templateUrl: '/users/login_form'
        controller: 'LoginModalController'

]