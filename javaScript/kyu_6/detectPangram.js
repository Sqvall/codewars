/** https://www.codewars.com/kata/545cedaa9943f7fe7b000048 */

const alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

function isPangram(string) {
  let result = 0;
  for (const i of alphabet) {
    string.toString().toUpperCase().indexOf(i) !== -1 && result++;
  }
  return result === alphabet.length;
}

isPangram('The quick brown fox jumps over the lazy dog.'); // true
isPangram('This is not a pangram.'); // false
