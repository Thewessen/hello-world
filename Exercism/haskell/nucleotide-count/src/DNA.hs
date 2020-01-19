module DNA (nucleotideCounts, Nucleotide(..)) where

import Data.Map (Map, fromList)

data Nucleotide = A | C | G | T deriving (Eq, Ord, Show)

nucleotideCounts :: String -> Either String (Map Nucleotide Int)
nucleotideCounts xs
  | any (not . flip elem "ACGT") xs = Left xs
  | otherwise = Right $ fromList [(x, count x) | x <- [A, C, G, T]]
                where count x = length $ filter (\c -> show x == [c]) xs
