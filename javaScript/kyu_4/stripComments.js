/** https://www.codewars.com/kata/51c8e37cee245da6b40000bd */

function solution(input, markers) {
  for (let i of markers) {
    if (i === '$') i = '\\$';
    const regExp = new RegExp(`( ${i}.*\\n)|(${i}.*$)`)
    input = input.replace(regExp, '\n')
  }
  return input.trim();
}

console.log(solution("apples, plums % and bananas\npears\noranges !applesauce", ["%", "!"])); // "apples, plums\npears\noranges")
console.log()
console.log(solution("Q @b\nu\ne -e f g", ["@", "-"])); // "Q\nu\ne")
console.log()
console.log(solution("a\nc\nd $e f g", ['#', '$'])); // 'a\nc\nd')
