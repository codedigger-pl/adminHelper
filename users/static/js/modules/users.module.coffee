angular.module 'adminHelper.users', ['adminHelper.users.services', 'adminHelper.users.controllers']

angular.module 'adminHelper.users.services', ['restangular']
angular.module 'adminHelper.users.controllers', ['ng.django.forms', 'restangular']
