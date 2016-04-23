(function() {
    'use strict';

    angular
        .module('app.commands')
        .controller('CommandsController', CommandsController);

    // 'isLoggedIn' is passed from the config.route.js
    CommandsController.$inject = ['$location', '$localStorage', 'isLoggedIn', 'CommandService', 'UserService'];

    function CommandsController($location, $localStorage, isLoggedIn, CommandService, UserService) {
        var vm = this;

        if (!isLoggedIn) {
            $location.path('/');
            return;
        }

        vm.commands = '';
        vm.username = $localStorage.username;

        commands();

        function commands() {
            var query = CommandService.query();
            query.$promise
                .then(function(data) {
                    vm.commands = data;
                }).catch(function(error) {
                    console.log(error);
                    vm.commands = error;
                });
        }
    }
})();
