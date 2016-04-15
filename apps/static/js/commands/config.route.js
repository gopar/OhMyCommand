(function() {
    'use strict';

    angular
        .module('app.commands')
        .config(configFunction);

    configFunction.$inject = ['$routeProvider', 'STATIC_URL'];

    function configFunction($routeProvider, STATIC_URL) {
        $routeProvider.when('/commands', {
            templateUrl: STATIC_URL + '/commands/commands.html',
            controller: 'CommandsController',
            controllerAs: 'vm',
            resolve: {isLoggedIn: resolveUser}
        });
    }

    resolveUser.$inject = ['authService'];

    function resolveUser(authService) {
        return authService.isLoggedIn();
    }
})();
