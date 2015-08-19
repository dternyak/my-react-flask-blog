'use strict';

/**
 * @ngdoc function
 * @name yoApp.controller:ProtectedCtrl
 * @description
 * # ProtectedCtrl
 * Controller of the yoApp
 */
angular.module('yoApp')
    .controller('ProtectedCtrl', function ($scope, $http) {
        $scope.htmlcontent = $scope.orightml;

        $scope.title = '';


        $scope.submit = function () {


            $http({
                url: '/create_posts',
                method: "POST",
                data: {
                    body: $scope.htmlcontent,
                    title: $scope.title,
                    image: $scope.image

                }
            }).success(function (data, status, headers, config) {
                console.log("great")
                alert("success")
                $scope.htmlcontent = ''
                $scope.title = ''

            }).error(function (data, status, headers, config) {
            });


        }


    });
