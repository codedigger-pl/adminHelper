// Generated by CoffeeScript 1.9.1
(function() {
  var overviewController;

  overviewController = angular.module('adminHelper.ACS.controllers');

  overviewController.controller('ACSOrderAddModalController', [
    '$scope', '$modalInstance', 'djangoForm', 'Restangular', 'sessionFactory', function($scope, $modalInstance, djangoForm, Restangular, sessionFactory) {
      var orderBase, ruleBase;
      ruleBase = Restangular.all('api/ACSRules');
      orderBase = Restangular.all('api/ACSOrders');
      $scope.ok = function() {
        var ruleRequest;
        ruleRequest = ruleBase.post({
          person: $scope.ACSRule.person,
          zone: $scope.ACSRule.zone
        });
        return ruleRequest.then(function(rule) {
          var orderRequest;
          orderRequest = orderBase.post({
            rule: rule.id,
            user: sessionFactory.user.id,
            grant_privilege: $scope.ACSOrder.grant_privilege
          });
          return orderRequest.then(function() {
            return $modalInstance.close();
          }, function(response) {
            if (response.status === 400) {
              return djangoForm.setErrors($scope.ACSOrderForm, response.data);
            }
          });
        }, function(response) {
          if (response.status === 400) {
            return djangoForm.setErrors($scope.ACSRuleForm, response.data);
          }
        });
      };
      return $scope.cancel = function() {
        return $modalInstance.dismiss('cancel');
      };
    }
  ]);

}).call(this);

//# sourceMappingURL=addACSOrder.controller.js.map