'use strict';

/**
 * @ngdoc overview
 * @name yoApp
 * @description
 * # yoApp
 *
 * Main module of the application.
 */
angular
    .module('yoApp', [
        'textAngular',

        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngTouch',
    ])

function posts($http, $q) {
    var deferred = $q.defer();
    var responsePromise = $http.get("/make_post");
    responsePromise.success(function (data, status, headers, config) {
        deferred.resolve(data);

    })
    return deferred.promise;

}


angular.module('yoApp').config(function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'app/views/home.html',

        })
        .when('/portfolio', {
            templateUrl: 'app/views/portfolio.html',

        })
        .when('/blog', {
            templateUrl: 'app/views/main.html',
            controller: 'MainCtrl',
            resolve: {
                "posts": posts
            }
        })

        .when('/posts/:param1', {
            templateUrl: 'app/views/post.html',
            controller: 'PostCtrl',


        })
        .when('/admin', {
            templateUrl: 'app/views/protected.html',
            controller: 'ProtectedCtrl',
            resolve: {
                //This function is injected with the AuthService where you'll put your authentication logic
                'auth': function (AuthService, $location, $rootScope) {
                    return AuthService.isLoggedIn()
                        .then(function () {
                            $rootScope.userIsAuthenticated = true;
                            console.log("continue")
                        })
                        .catch(function () {
                            $location.path('/');

                        });
                }
            }

        })
        .when('/your_posts', {
            templateUrl: 'app/views/your_posts.html',
            controller: 'YourPostsCtrl',
            resolve: {
                //This function is injected with the AuthService where you'll put your authentication logic
                'auth': function (AuthService, $location, $rootScope) {
                    return AuthService.isLoggedIn()
                        .then(function () {
                            $rootScope.userIsAuthenticated = true;
                            console.log("continue")
                        })
                        .catch(function () {
                            $location.path('/');

                        });
                }
            }

        })
        .when('/your_posts', {
            templateUrl: 'app/views/your_posts.html',
            controller: 'YourPostsCtrl',
            resolve: {
                //This function is injected with the AuthService where you'll put your authentication logic
                'auth': function (AuthService, $location, $rootScope) {
                    return AuthService.isLoggedIn()
                        .then(function () {
                            $rootScope.userIsAuthenticated = true;
                            console.log("continue")
                        })
                        .catch(function () {
                            $location.path('/');

                        });
                }
            }

        })
        .when('/your_posts/:param1', {
            templateUrl: 'app/views/your_posts_update.html',
            controller: 'YourPostsUpdateCtrl',
            resolve: {
                //This function is injected with the AuthService where you'll put your authentication logic
                'auth': function (AuthService, $location, $rootScope) {
                    return AuthService.isLoggedIn()
                        .then(function () {
                            $rootScope.userIsAuthenticated = true;
                            console.log("continue")
                        })
                        .catch(function () {
                            $location.path('/');

                        });
                }
            }

        })

        .when('/logout', {
            templateUrl: 'app/views/logout.html',
            controller: 'LogoutCtrl',
            resolve: {
                //This function is injected with the AuthService where you'll put your authentication logic
                'auth': function (AuthService, $location, $rootScope) {
                    return AuthService.isLoggedIn()
                        .then(function () {
                            $rootScope.userIsAuthenticated = true;
                            console.log("continuing")

                        })
                        .catch(function () {
                            console.log("cach")
                            $location.path('/login');
                        });
                }
            }
        })

        .otherwise({
            redirectTo: '/'
        });
})

