'use strict';

describe('Controller: LoginCallbackCtrl', function () {

  // load the controller's module
  beforeEach(module('yoApp'));

  var LoginCallbackCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    LoginCallbackCtrl = $controller('LoginCallbackCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(LoginCallbackCtrl.awesomeThings.length).toBe(3);
  });
});
