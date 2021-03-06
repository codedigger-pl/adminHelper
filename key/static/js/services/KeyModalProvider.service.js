// Generated by CoffeeScript 1.9.1
(function() {
  var modalFactory;

  modalFactory = angular.module('adminHelper.key.services');

  modalFactory.factory('KeyModalFactory', [
    '$modal', function($modal) {
      var ModalFactory;
      return new (ModalFactory = (function() {
        function ModalFactory() {}

        ModalFactory.prototype.openKeyAddModal = function() {
          return $modal.open({
            templateUrl: '/key/addKey',
            controller: 'KeyAddModalController'
          });
        };

        ModalFactory.prototype.openKeyOrderAddModal = function() {
          return $modal.open({
            templateUrl: '/key/addKeyOrder',
            controller: 'KeyOrderAddModalController'
          });
        };

        ModalFactory.prototype.openKeyRequestAddModal = function() {
          return $modal.open({
            templateUrl: '/key/addKeyRequest',
            controller: 'KeyRequestAddModalController'
          });
        };

        return ModalFactory;

      })());
    }
  ]);

}).call(this);

//# sourceMappingURL=KeyModalProvider.service.js.map
