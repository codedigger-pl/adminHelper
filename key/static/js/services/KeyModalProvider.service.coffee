modalFactory = angular.module 'adminHelper.key.services'

modalFactory.factory 'KeyModalFactory', ['$modal', ($modal) ->
  new class ModalFactory

    openKeyAddModal: ->
      $modal.open
        templateUrl: '/key/addKey'
        controller: 'KeyAddModalController'

    openKeyOrderAddModal: ->
      $modal.open
        templateUrl: '/key/addKeyOrder'
        controller: 'KeyOrderAddModalController'

    openKeyRequestAddModal: ->
      $modal.open
        templateUrl: '/key/addKeyRequest'
        controller: 'KeyRequestAddModalController'

]