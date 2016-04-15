(function() {
    'use strict';

    angular
        .module('app.auth')
        .factory('authService', authService);

    authService.$inject = ['$resource'];

    function authService($resource) {
        var service = {
            login: login,
            register: register
        };
        return service;

        ////////////////////
        function login(user) {
            return $resource('/api-token-auth/').save({
                username: user.username,
                password: user.password
            });
        }

        function register(user) {
            return $resource('/api/users/').save({
                username: user.username,
                password: user.password,
                email: user.email
            });
        }
    }
})();
