'use strict';

/**
 * @ngdoc function
 * @name yoApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the yoApp
 */
angular.module('yoApp')
  .controller('PostCtrl', function ($scope, $window, $http, $routeParams) {


        var post = $routeParams.param1;

        $scope.post = '';

        $http({
                url: '/get_single_post',
                method: "POST",
                data: {
                    id: post,

                }
            }).success(function (data, status, headers, config) {

            $scope.post = data;
            console.log($scope.post)
            }).error(function (data, status, headers, config) {
            });


  });
