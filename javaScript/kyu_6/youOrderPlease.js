/** https://www.codewars.com/kata/55c45be3b2079eccff00010f/ */

const order = (words) => {
  words = words.split(' ')
  const result = words.map((item, index) => {
    for (const j of words) {
      if (j.split('').indexOf(String(index + 1)) !== -1) {
        words.splice(words.indexOf(j), 1, '')
        return j
      }
    }
  })
  return result.join(' ')
}

