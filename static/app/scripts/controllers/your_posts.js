'use strict';

/**
 * @ngdoc function
 * @name yoApp.controller:ProtectedCtrl
 * @description
 * # ProtectedCtrl
 * Controller of the yoApp
 */
angular.module('yoApp')
    .controller('YourPostsCtrl', function ($scope, $http) {
        $scope.posts = '';
        $http.get("/your_posts")

            .success(function (data, status, headers, config) {
                $scope.posts = data;

            }).error(function (data, status, headers, config) {

            });





    });
