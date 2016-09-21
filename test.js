// load Unit.js module
var test = require('unit.js'),
    check = require('./my_modules/check.js');

/* Testing for custom modules */
describe('Testing for my custom modules:', function(){
  // test boolean
  it('Is the given positive integer prime?', function(){
    test.assert(check.isPrime(2349));
  });
  it('Is the given positive integer prime?', function(){
    test.value(check.isPrime(19))
        .is(true);
  });

  // test string
  it('Is the type of given var "string"?', function(){
    // just for example of tested value
    var example = 'hello world';
    // assert that example variable is a string
    test.string(example);
  });

  // test obj
  it('Is the given variable an object?', function(){
    //
    var obj = {first_name: 'Alan', last_name: 'Tai'};
    test.object(obj)
        .hasOwnProperty('last_name')
        .hasOwnProperty('first_name');
  });
});

/* Testing for API App */
var request = require('supertest');
var app = require('./index.js');

// test GET
describe('GET /user', function(){
  it('respond with json', function(done){
    request(app).get('/user')
                .set('Accept', 'application/json')
                .expect('Content-Type', 'application/json; charset=utf-8')
                .expect(200, {first_name: 'Alan', last_name: 'Tai'}, done);
  });
});

// test POST
describe('POST /is-prime', function(){
  it('respond with true/false for checking if given number is prime', function(done){
    request(app).post('/is-prime')
                .type('json')
                .send({ num: 52 })
                .set('Accept', 'application/json')
                .expect('Content-Type', 'application/json; charset=utf-8')
                .expect(200, {is_prime: true}, done);
  });
});
