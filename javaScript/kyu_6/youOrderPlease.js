/** https://www.codewars.com/kata/55c45be3b2079eccff00010f/ */

const order = (words) => {
  const result = words.split(' ').sort((a, b) => a.match(/\d+/) - b.match(/\d+/))
  return result.join(' ')
}

console.log(order("is2 Thi1s T4est 3a")); // "Thi1s is2 3a T4est"
