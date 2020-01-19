module DNA (toRNA) where

toRNA :: String -> Either Char String
toRNA rna@(x:xs)
  | rna == "" = Right ""
  | x == 'C' = ('G'++) <$> toRNA xs
  | x == 'G' = ('C'++) <$> toRNA xs
  | x == 'T' = ('A'++) <$> toRNA xs
  | x == 'A' = ('U'++) <$> toRNA xs
  | otherwise = Left x
