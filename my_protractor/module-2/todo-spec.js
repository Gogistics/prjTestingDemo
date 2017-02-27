/* Protractor Example from Offcial Website */
// describe, it, and expect are from Jasmine
// browser, element, and by are basic objects of Protractor
// browser
describe('Protractor Demo App', function() {
  var firstNumber = element(by.model('first')),
    secondNumber = element(by.model('second')),
    goButton = element(by.id('gobutton')),
    latestResult = element(by.binding('latest'));

  beforeEach(function() {
    browser.get('http://juliemr.github.io/protractor-demo/');
  });

  it('should have a title', function() {
    expect(browser.getTitle()).toEqual('Super Calculator');
  });

  // successful case
  it('should add one and two', function() {
    firstNumber.sendKeys(1);
    secondNumber.sendKeys(2);

    goButton.click();

    expect(latestResult.getText()).toEqual('3');
  });

  // failed
  it('should add four and six', function() {
    // Fill this in.
    expect(latestResult.getText()).toEqual('0');
  });
});