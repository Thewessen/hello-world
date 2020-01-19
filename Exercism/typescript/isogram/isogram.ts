class Isogram {
  static isIsogram(word: string): boolean {
    return !/([a-z]).*\1/.test(word.toLowerCase())
  }
}

export default Isogram
