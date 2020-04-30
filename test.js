const arrayDiff = (a, b) => {
  let result = new Set(a)
  for (let i of b) {
    result.delete(i)
  }
  return result;
}

console.log(arrayDiff([], [4, 5])); // [], "a was [], b was [4,5]")
console.log(arrayDiff([3, 4], [3])); // [4], "a was [3,4], b was [3]")
console.log(arrayDiff([1, 8, 2], [])); // [1,8,2], "a was [1,8,2], b was []")
