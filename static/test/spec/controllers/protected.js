'use strict';

describe('Controller: ProtectedCtrl', function () {

  // load the controller's module
  beforeEach(module('yoApp'));

  var ProtectedCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ProtectedCtrl = $controller('ProtectedCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ProtectedCtrl.awesomeThings.length).toBe(3);
  });
});
