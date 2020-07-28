/** https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/ */

const ipToInt32 = (ip) => (ip.split('.').reduce((a, v) => (a * 256 + (+v)))); // (+v) string to number

console.log(ipToInt32("128.32.10.1")); // return: 2149583361
