(function() {
    'use strict';

    var app = angular.module('app.commands');

    app.factory('CommandService', CommandService);
    app.factory('UserService', UserService);

    CommandService.$inject = ['$resource'];
    function CommandService($resource) {
        return {
            command: function(token) {
                return $resource('/api/commands/:id/', null, {
                    query: {
                        method: 'GET',
                        isArray: true,
                        headers: {
                            'Authorization': 'Token ' + token
                        }
                    },
                    save: {
                        method: 'POST',
                        isArray: false,
                        headers: {
                            'Authorization': 'Token ' + token
                        }
                    },
                    delete: {
                        method: 'DELETE',
                        isArray: false,
                        headers: {
                            'Authorization': 'Token ' + token
                        }
                    }
                });
            }
        };
    }

    UserService.$inject = ['$resource'];
    function UserService($resource) {
        return $resource('/api/users/:id/');
    }
})();
