/** https://www.codewars.com/kata/5267faf57526ea542e0007fb */

Math.floor = function(number) {
  return parseInt(number)
};

Math.ceil = function(number) {
  return parseInt(number) === number ? number : Math.floor(number) + 1
};

Math.round = function(number) {
  return number % 1 < 0.5 ? Math.floor(number) : Math.ceil(number)
};

console.log(Math.round(0.4))  // 0 'Math.round(0.4)'
console.log(Math.round(0.5))  // 1 'Math.round(0.5)'

console.log(Math.ceil(0.4));  // 1 'Math.ceil(0.4)'
console.log(Math.ceil(0.5));  // 1 'Math.ceil(0.5)'

console.log(Math.floor(0.4))  // 0 'Math.floor(0.4)'
console.log(Math.floor(0.5));  // 0 'Math.floor(0.5)'
