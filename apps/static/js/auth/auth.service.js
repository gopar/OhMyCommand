(function() {
    'use strict';

    angular
        .module('app.auth')
        .factory('authService', authService);

    authService.$inject = ['$resource', '$localStorage'];

    function authService($resource, $localStorage) {
        var service = {
            login: login,
            register: register,
            isLoggedIn: isLoggedIn
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

        function isLoggedIn() {
            if ($localStorage.hasOwnProperty('token')) {
                if ($localStorage.token != '')
                    return true;
            }
            return false;
        }
    }
})();
