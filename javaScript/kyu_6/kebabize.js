/** https://www.codewars.com/kata/57f8ff867a28db569e000c4a */

function kebabize(str) {
  str = str.replace(/[0-9]/g, '');
  let result = '';
  for (let i of str) {
    if (i === i.toUpperCase() && str.indexOf(i) !== 0) result += `-${i.toLowerCase()}`;
    else result += i.toLowerCase();
  }
  return result
}

console.log(kebabize('myCamelCasedString')); //, 'my-camel-cased-string');
console.log(kebabize('myCamelHas3Humps')); //, 'my-camel-has-humps');
console.log(kebabize('C14hh')); // 'chh'
