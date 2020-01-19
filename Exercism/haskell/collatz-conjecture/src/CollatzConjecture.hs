module CollatzConjecture (collatz) where

collatz :: Integer -> Maybe Integer
collatz n
  | n == 1 = Just 0
  | n < 1 = Nothing
  | even n = (1+) <$> collatz (div n 2)
  | odd n = (1+) <$> collatz (3 * n + 1)
  | otherwise = Nothing
