let len = String.length
let low = String.lowercase_ascii
let tail = (word, n) => String.sub(word, n, word->len - n)

let removeChar = (word, char) => {
  let i = String.index(word, char)
  String.sub(word, 0, i) ++ word->tail(i + 1)
}

let rec sameLetters = (word1, word2) =>
  switch (word1.[0]) {
    | exception Invalid_argument(_) => true
    | char when !String.contains(word2, char) => false
    | char => sameLetters(word1->tail(1), word2->removeChar(char))
  }

let isAnagram = (word1, word2) =>
  word1->len == word2->len &&
  word1->low != word2->low &&
  sameLetters(word1->low, word2->low)

let anagrams = (word, candidates) => candidates |> List.filter(isAnagram(word))

