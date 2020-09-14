/** https://www.codewars.com/kata/523f5d21c841566fde000009/ */

const arrayDiff = (a, b) => {
  b.map(itemB => a = a.filter(itemA => itemB !== itemA))
  return a;
}

console.log(arrayDiff([], [4, 5])); // [], "a was [], b was [4,5]")
console.log(arrayDiff([3, 4], [3])); // [4], "a was [3,4], b was [3]")
console.log(arrayDiff([1, 8, 2], [])); // [1,8,2], "a was [1,8,2], b was []")

// This not mine, but interesting

function array_diff(a, b) {
  return a.filter(e => !b.includes(e));
}
