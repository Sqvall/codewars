/** https://www.codewars.com/kata/52597aa56021e91c93000cb0/solutions/javascript */

const moveZeros = (arr) => {
  return [...arr.filter(i => i !== 0), ...arr.filter(i => i === 0)]
}

console.log(moveZeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]));
console.log(moveZeros([1, 2, 1, 1, 3, 1, 0, 0, 0, 0]));
