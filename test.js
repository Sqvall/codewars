const words = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

const addParagrapg = (wordIndex) => {
  return `${words[wordIndex]} green bottle${words[wordIndex] === 'One' ? '' : 's'} hanging on the wall,
Two green bottle${words[wordIndex] === 'One' ? '' : 's'} hanging on the wall,
${words[wordIndex] === 'One' ? 'If that' : 'And if'} one green bottle should accidentally fall,
There'll be ${words[wordIndex] === 'One' ? 'no' : words[wordIndex - 1].toLowerCase()} green bottle hanging on the wall.\n`
}

const tenGreenBottles = (n) => {
  let result = ''
  for (let i = 6; i < 0; i--) {
    console.log(i)
    result += addParagrapg(i)
    if (i !== 0) {
      result += '\n'
    }
  }
  return result;
}

tenGreenBottles(2)
