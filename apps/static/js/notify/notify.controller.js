(function() {
    'use strict';

    angular
        .module('app.notify')
        .controller('NotifyController', NotifyController);

    NotifyController.$inject = ['notifyService'];

    function NotifyController(notifyService) {
        var vm = this;
        vm.notifyService = notifyService;
    }
})();
