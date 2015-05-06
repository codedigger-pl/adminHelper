# namespace
overviewController = angular.module 'adminHelper.users.controllers'

###
  Controller PersonList

  Angular controller for person list view.
###
overviewController.controller 'PersonDetailController', [
  '$scope'
  '$stateParams'
  'djangoForm'
  'Restangular'
  'sessionFactory'
  ($scope, $stateParams, djangoForm, Restangular, sessionFactory) ->
    base = Restangular.one('api/persons', $stateParams.id)
    alarmOrderBase = Restangular.all('api/alarmOrders')
    alarmRequestBase = Restangular.all('api/alarmRequests')
    alarmRuleBase = Restangular.all('api/alarmRules')
    alarmZoneBase = Restangular.all('api/alarmZones')

    ACSOrderBase = Restangular.all('api/ACSOrders')
    ACSRequestBase = Restangular.all('api/ACSRequests')
    ACSRuleBase = Restangular.all('api/ACSRules')
    ACSZoneBase = Restangular.all('api/ACSZones')

    $scope.person = base.get().$object
    $scope.alarmZones = base.getList('alarm_zones').$object
    $scope.ACSZones = base.getList('acs_zones').$object

    if not $scope.person.photo
      $scope.person.photo = '/static/img/unknown_user.jpg'

    $scope.updateCardNumber = ->
      request = $scope.person.patch
        card_number: $scope.person.card_number
      request.then \
        (person) ->
          $scope.person = person
        ,
        (response) ->
          if response.status == 400
            djangoForm.setErrors($scope.cardNumberForm, response.data)

    $scope.updateData = ->
      request = $scope.person.patch
        first_name: $scope.person.first_name
        last_name: $scope.person.last_name
        rank: $scope.person.rank
        group: $scope.person.group
      request.then \
        (person) ->
          $scope.person = person
        ,
        (response) ->
          if response.status == 400
            djangoForm.setErrors($scope.dataForm, response.data)

    $scope.updatePhoto = ->
      # FormData: only by PUT request?
      console.log('updatePhoto called')

    $scope.addToAlarmZone = (zoneID, grant) ->
      personID = $stateParams.id

      alarmZoneBase.get(zoneID).then (zone) ->
        ruleResp = alarmRuleBase.post
          person: personID
          zone: zone.id
        ruleResp.then (ruleResp) ->
          currBase = null
          if sessionFactory.user.id == zone.manager
            currBase = alarmOrderBase
          else
            currBase = alarmRequestBase
          currBase.post
            rule: ruleResp.id
            user: sessionFactory.user.id
            grant_privilege: grant

    $scope.addToACSZone = (zoneID, grant) ->
      personID = $stateParams.id

      ACSZoneBase.get(zoneID).then (zone) ->
        ruleResp = ACSRuleBase.post
          person: personID
          zone: zone.id
        ruleResp.then (ruleResp) ->
          currBase = null
          if sessionFactory.user.id == zone.manager
            currBase = ACSOrderBase
          else
            currBase = ACSRequestBase
          currBase.post
            rule: ruleResp.id
            user: sessionFactory.user.id
            grant_privilege: grant

]
