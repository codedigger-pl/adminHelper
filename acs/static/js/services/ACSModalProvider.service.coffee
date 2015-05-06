modalFactory = angular.module 'adminHelper.ACS.services'

modalFactory.factory 'ACSModalFactory', ['$modal', ($modal) ->
  new class ModalFactory

    openACSZoneAddModal: ->
      $modal.open
        templateUrl: '/acs/addACSZone'
        controller: 'ACSZoneAddModalController'

    openACSOrderAddModal: ->
      $modal.open
        templateUrl: '/acs/addACSOrder'
        controller: 'ACSOrderAddModalController'

    openACSRequestAddModal: ->
      $modal.open
        templateUrl: '/acs/addACSRequest'
        controller: 'ACSRequestAddModalController'

]