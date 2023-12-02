// 1160. Find Words That Can Be Formed by Characters
/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function (words, chars) {
  const charsCounter = Array(26);
  let counter = 0;
  for (let i = 0; i < chars.length; i++) {
    charsCounter[chars.codePointAt(i) - 97] =
      (charsCounter[chars.codePointAt(i) - 97] || 0) + 1;
  }

  for (const word of words) {
    let isValidWord = true;
    const newCounter = [...charsCounter];

    for (let i = 0; i < word.length; i++) {
      if (
        !newCounter[word.codePointAt(i) - 97] ||
        newCounter[word.codePointAt(i) - 97] === 0
      ) {
        isValidWord = false;
        break;
      }
      newCounter[word.codePointAt(i) - 97]--;
    }

    if (isValidWord) {
      counter += word.length;
    }
  }

  return counter;
};
