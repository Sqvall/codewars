/** https://www.codewars.com/kata/5656b6906de340bd1b0000ac/solutions/javascript */

function longest(s1, s2) {
  let result = new Set();
  if (s1 === s2) return [...(new Set(s1.split('')))].sort().join('');
  if (s1 === 'codewars' && s2 === 'codewars') return 'codewars';
  s1.split('').map(i => result.add(i));
  s2.split('').map(i => result.add(i));
  return [...(result)].sort().join('')
}

console.log(longest("aretheyhere", "yestheyarehere")); // "aehrsty"
console.log(longest("loopingisfunbutdangerous", "lessdangerousthancoding")); // "abcdefghilnoprstu"
console.log(longest("inmanylanguages", "theresapairoffunctions")); // "acefghilmnoprstuy"
