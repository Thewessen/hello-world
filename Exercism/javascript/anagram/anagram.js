'use strict'

const norm = (str) =>
  [...str].sort().join().toLowerCase()

const sameLetters = (s) => (w) =>
  norm(s) === norm(w)

const notSameWord = (s) => (w) => 
  s.toLowerCase() !== w.toLowerCase()

export class Anagram {
  constructor(word) {
    this.subject = word.toLowerCase()
  }

  matches (list) {
    return list
      .filter(notSameWord(this.subject))
      .filter(sameLetters(this.subject))
  }
}
