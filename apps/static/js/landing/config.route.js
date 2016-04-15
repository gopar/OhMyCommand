(function () {
    'use strict';

    angular
        .module('app.landing')
        .config(configFunction);

    configFunction.$inject = ['$routeProvider', 'STATIC_URL'];

    function configFunction($routeProvider, STATIC_URL) {
        $routeProvider.when('/', {
            templateUrl: STATIC_URL + '/landing/landing.html'
        });
    }
})();
