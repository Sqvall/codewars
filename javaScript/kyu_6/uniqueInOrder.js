const uniqueInOrder = (iterable) => {
  return [...iterable].filter((item, index) => iterable[index - 1] !== item)
}

console.log(uniqueInOrder('AAAABBBCCDAABBB')); // ['A','B','C','D','A','B']
console.log(uniqueInOrder([2, 4, 4, 1, 1, 5, 1])); // [2, 4, 1, 5, 1]
