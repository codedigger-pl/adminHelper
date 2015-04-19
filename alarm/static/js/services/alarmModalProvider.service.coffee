modalFactory = angular.module 'adminHelper.alarm.services'

modalFactory.factory 'alarmModalFactory', ['$modal', ($modal) ->
  new class ModalFactory

    openAlarmZoneAddModal: ->
      $modal.open
        templateUrl: '/alarm/addAlarmZone'
        controller: 'AlarmZoneAddModalController'

]