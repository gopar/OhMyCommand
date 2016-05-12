(function() {
    'use strict';

    angular
        .module('app.commands')
        .controller('CommandsController', CommandsController);

    // 'isLoggedIn' is passed from the config.route.js
    CommandsController.$inject = ['$location', '$localStorage', '$timeout', 'isLoggedIn', 'CommandService', 'UserService', 'notifyService'];

    function CommandsController($location, $localStorage, $timeout, isLoggedIn, CommandService, UserService, notifyService) {
        var vm = this;

        if (!isLoggedIn) {
            $location.path('/');
            return;
        }

        vm.commands = '';
        vm.username = $localStorage.username;
        vm.deleteCommand = deleteCommand;
        vm.newCommand = newCommand;
        vm.updateCommand = updateCommand;
        vm.copyCommand = copyCommand;

        vm.new = {
            command: '',
            os:  '',
            version: '',
            note: ''
        };

        vm.edit = {
            command: '',
            os:  '',
            version: '',
            note: ''
        };

        commands();

        ////////////////////
        function commands() {
            var query = CommandService.command($localStorage.token).query();
            query.$promise
                .then(function(data) {
                    vm.commands = data;
                }).catch(function(error) {
                    console.log(error);
                    vm.commands = error;
                });
        }

        function deleteCommand(command) {
            var i;
            for (i = 0; i < vm.commands.length; i++)
                if(vm.commands[i].id === command.id)
                    break;

            var query = CommandService.command($localStorage.token).delete({id: command.id});
            query.$promise
                .then(function(data) {
                    vm.commands.splice(i, 1);
                }).catch(function(error) {
                    console.log(error);
                });
        }

        function newCommand() {
            // TODO: Error checking must have at least 'command' filled out
            if (vm.new.command === '')
                return;

            var query = CommandService.command($localStorage.token).save({
                command: vm.new.command,
                os: vm.new.os,
                version: vm.new.version,
                note: vm.new.note
            });

            query.$promise
                .then(function(data) {
                    vm.commands.unshift(data);
                    $('#newCommandModal').modal('hide');
                    notifyService.display('Added New Command');
                    $timeout(function() {
                        notifyService.showMessage = false;
                    }, 3000);
                })
                .catch(function(error) {
                    console.log(error);
                });
        }

        function updateCommand() {
            var i;
            for(i = 0; i < vm.commands.length; i++)
                if (vm.commands[i].id === vm.edit.id)
                    break;
            // No reason to send update request if objects are still the same
            if (angular.equals(vm.commands[i], vm.edit))
                return;

            var query = CommandService.command($localStorage.token).update({id: vm.edit.id}, {
                command: vm.edit.command,
                os: vm.edit.os,
                version: vm.edit.version,
                note: vm.edit.note
            });

            query.$promise
                .then(function(response) {
                    vm.commands[i] = vm.edit;
                    $('#updateCommandModal').modal('hide');
                    notifyService.display('Updated Command');
                    $timeout(function() {
                        notifyService.showMessage = false;
                    }, 3000);
                })
                .catch(function(error) {
                    console.log(error);
                });
        }

        function copyCommand(command) {
            vm.edit = angular.copy(command);
        }
    }
})();
