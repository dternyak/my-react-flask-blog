'use strict';

/**
 * @ngdoc function
 * @name yoApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the yoApp
 */
angular.module('yoApp')
  .controller('LoginCtrl', function ($scope, $window, $http) {

      $scope.signIn = function() {

            var responsePromise = $http.get("/test");
            responsePromise.success(function (data, status, headers, config) {

              console.log(data.url)
            $window.location.href= data.url


            });

            responsePromise.error(function (data, status, headers, config) {
                alert("AJAX failed!");
            });
        }

  });
