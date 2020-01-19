module SumOfMultiples (sumOfMultiples) where

sumOfMultiples :: [Integer] -> Integer -> Integer
sumOfMultiples factors limit = sum [x |
                                    x <- (take (fromIntegral limit - 1) [1..]),
                                    any (x %%) factors]
                               where (%%) x y
                                       | x == 0 || y == 0 = False
                                       | otherwise = x `mod` y == 0
