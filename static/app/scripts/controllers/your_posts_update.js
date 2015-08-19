'use strict';

/**
 * @ngdoc function
 * @name yoApp.controller:ProtectedCtrl
 * @description
 * # ProtectedCtrl
 * Controller of the yoApp
 */
angular.module('yoApp')
    .controller('YourPostsUpdateCtrl', function ($scope, $http, $routeParams) {


        var post = $routeParams.param1;


        $http({
            url: '/get_single_post',
            method: "POST",
            data: {
                id: post,

            }
        })
            .success(function (data, status, headers, config) {

                $scope.htmlcontent = data.body;

                $scope.title = data.title;


                $scope.submit = function () {
                    $http({
                        url: '/update_post',
                        method: "POST",
                        data: {
                            body: $scope.htmlcontent,
                            title: $scope.title,
                            id: post

                        }
                    }).success(function (data, status, headers, config) {
                        if (data === "Success") {
                            alert("success")

                        }

                    }).error(function (data, status, headers, config) {
                    });


                }


            }).error(function (data, status, headers, config) {

            });


    });
