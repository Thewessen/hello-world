module Acronym (abbreviate) where

import Data.Char (isSeperator, isPunctuation)

abbreviate :: String -> String
abbreviate xs = error "You need to implement this function."

words' :: String -> [String]
words' "" = [""]
words' (x:xs)
  | isSeperator x || isPunctuation x = [[x] 
  | otherwise = [([x]:) words' xs]
