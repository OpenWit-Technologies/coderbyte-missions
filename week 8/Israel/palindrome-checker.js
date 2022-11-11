function Palindrome (str) {
  var stringReplaced = str.replace(/\s/g, '')
  var checkPalindrome = str
    .split('')
    .reverse()
    .join('')
    .replace(/\s/g, '')

  if (checkPalindrome === stringReplaced) {
    return true
  } else {
    // code goes here
    return false
  }
}

// keep this function call here
console.log(Palindrome(readline()))
