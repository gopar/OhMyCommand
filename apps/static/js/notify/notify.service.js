(function() {
    'use strict';

    angular
        .module('app.notify')
        .service('notifyService', notifyService);

    function notifyService() {
        var vm = this;

        vm.message = '';
        vm.showMessage = false;
        vm.display = display;

        ////////////////////
        function display(m) {
            vm.message = m;
            vm.showMessage = true;
        }
    }
})();
