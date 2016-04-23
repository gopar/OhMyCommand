(function() {
    'use strict';

    angular
        .module('app.auth')
        .controller('AuthController', AuthController);

    AuthController.$inject = ['$location', '$localStorage', 'authService'];

    function AuthController($location, $localStorage, authService) {
        var vm = this;

        vm.login = login;
        vm.logout = logout;
        vm.register = register;
        vm.isLoggedIn = isLoggedIn;
        // TODO: Save all these in $localStorage
        vm.user = {
            username: '',
            email: '',
            password: ''
        };

        function login(user) {
            var resource = authService.login(user);
            resource.$promise
                .then(function(response) {
                    $localStorage.token = response.token;
                    $localStorage.username = user.username;
                    $location.path('/commands');
                })
                .catch(function(error) {
                    console.log(error);
                });
        }

        function logout() {
            $localStorage.token = '';
            $localStorage.username = '';
            $location.path('/');
        }

        function register(user) {
            var resource = authService.register(user);
            resource.$promise
                .then(function(response) {
                    $localStorage.token = response.token;
                    $localStorage.username = user.username;
                })
                .catch(function(error) {
                    console.log(error);
                });
        }

        function isLoggedIn() {
            return authService.isLoggedIn();
        }
    }
})();
