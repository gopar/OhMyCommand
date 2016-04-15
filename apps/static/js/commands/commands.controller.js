(function() {
    'use strict';

    angular
        .module('app.commands')
        .controller('CommandsController', CommandsController);

    // 'User' is passed from the config.route.js
    CommandsController.$inject = ['$location', 'isLoggedIn'];

    function CommandsController($location, isLoggedIn) {
        var vm = this;

        if (!isLoggedIn) {
            $location.path('/');
            return;
        }
    }
})();
