(function() {
    'use strict';

    var app = angular.module('app.commands');

    app.factory('CommandService', CommandService);
    app.factory('UserService', UserService);

    CommandService.$inject = ['$resource'];
    function CommandService($resource) {
        return $resource('/api/commands/:id');
    }

    UserService.$inject = ['$resource'];
    function UserService($resource) {
        return $resource('/api/users/:id');
    }
})();
