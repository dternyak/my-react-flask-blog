'use strict';

/**
 * @ngdoc function
 * @name yoApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the yoApp
 */
angular.module('yoApp')
    .controller('MainCtrl', function ($scope, $http) {
        $scope.posts = '';

        var responsePromise = $http.get("/make_post");
        responsePromise.success(function (data, status, headers, config) {
            console.log(data)
            $scope.posts = data
        })

    });
