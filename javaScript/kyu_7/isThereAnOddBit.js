/** https://www.codewars.com/kata/5d6f49d85e45290016bf4718/solutions/javascript */

function anyOdd(x) {
  let result = parseInt(x).toString(2);
  if (result.length % 2 === 1) {
    result = '0' + result;
  }
  result = result.split('').some((item, index) => (index + 1) % 2 === 1 && item === '1');
  return result ? 1 : 0;
}

console.log(anyOdd(2863311530)); // 1);
console.log(anyOdd(128)); // 1;
console.log(anyOdd(131)); // 1;
console.log(anyOdd(2)); // 1;
console.log(anyOdd(24082)); // 1;
console.log(anyOdd(0)); // 0;
console.log(anyOdd(85)); // 0;
console.log(anyOdd(1024)); // 0;
console.log(anyOdd(1)); // 0;
console.log(anyOdd(1365)); // 0;
