angular.module('yoApp').factory('AuthService',
    ['$q', '$timeout', '$http', '$rootScope', '$window', '$location',
        function ($q, $timeout, $http, $rootScope, $window, $location) {


            // return available functions for use in controllers
            return ({
                isLoggedIn: isLoggedIn
            });

            function isLoggedIn() {
                var config = {headers: {
                    'Access-Control-Allow-Origin': '*'

        }
    };

                    var deferred = $q.defer();

                var responsePromise = $http.get("/is_logged_in", config);
                responsePromise.success(function (data, status, headers, config) {
                    if (data === "Success") {
                        console.log("Success");
                        deferred.resolve();


                    }
                    else  {
                    deferred.reject();

                    }

                });

                responsePromise.error(function (data, status, headers, config) {
                    return false;
                });


                        return deferred.promise;


            }
        }]);