'use strict'

export class Words {
  count (sentence) {
    return sentence
      .trim()
      .toLowerCase()
      .split(/\s+/)
      .reduce((obj, word) => {
        obj[word] = obj.hasOwnProperty(word)
          ? obj[word] + 1
          : 1
        return obj
      }, {})
  }
}
