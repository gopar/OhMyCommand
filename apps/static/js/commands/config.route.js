(function () {
    'use strict';

    angular
        .module('app.commands')
        .config(configFunction);

    configFunction.$inject = ['$routeProvider', 'STATIC_URL'];

    function configFunction($routeProvider, STATIC_URL) {
        $routeProvider.when('/commands', {
            templateUrl: STATIC_URL + '/commands/commands.html'
        });
    }
})();
