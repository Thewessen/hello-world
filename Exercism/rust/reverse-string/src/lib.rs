use unicode_reverse::reverse_grapheme_clusters_in_place;

pub fn reverse(input: &str) -> String {
  let mut string = String::from(input).as_mut_str();
  reverse_grapheme_clusters_in_place(string);
  string.slice()
}
