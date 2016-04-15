(function () {
    'use strict';

    angular.module('app', [
        // Angular modules
        'ngRoute',
        'ngResource',
        'ngStorage',
        // Custom modules
        'app.auth',
        'app.core',
        'app.commands',
        'app.landing',
    ]);
})();
