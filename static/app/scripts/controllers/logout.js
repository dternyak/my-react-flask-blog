'use strict';

/**
 * @ngdoc function
 * @name yoApp.controller:LogoutCtrl
 * @description
 * # LogoutCtrl
 * Controller of the yoApp
 */
angular.module('yoApp')
    .controller('LogoutCtrl', function ($http, $window, $scope) {

        $scope.Logout = function () {

            var responsePromise = $http.get("/test");
            responsePromise.success(function (data, status, headers, config) {
                console.log(data.url);
                $window.location.href = data.url

            });

            responsePromise.error(function (data, status, headers, config) {
                alert("AJAX failed!");
            });
        }
    });
