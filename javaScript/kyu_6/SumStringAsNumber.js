/** https://www.codewars.com/kata/5324945e2ece5e1f32000370 */

const sumStrings = (a, b) => {
  const aa = a.split('')
  const bb = b.split('')
  const result = []
  let carry = 0
  let i = Math.max(a.length, b.length)

  while (i--) {
    carry += (+aa.pop() || 0) + (+bb.pop() || 0);
    result.unshift(carry % 10);
    carry = Math.floor(carry / 10);
  }
  while (carry) {
    result.unshift(carry % 10);
    carry = Math.floor(carry / 10);
  }
  while (result[0] === 0) {
    result.shift()
  }
  return result.join('');
}

console.log(sumStrings('123', '456')); // '579'
console.log(sumStrings('025758799787848317800780717075', '954697598010266789361008499836')); // '980456397798115107161789216911'
