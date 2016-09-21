module.exports = {
  isPrime: function(arg_number){
    //
    var factors = [];
    for(var ith = Math.floor(Math.sqrt(arg_number)); ith > 1 ; ith--){
      // check if factor exists
      if(arg_number % ith === 0) factors.push(ith);
    }
    return (factors.length <= 0);
  }
}
