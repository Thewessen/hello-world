module ArmstrongNumbers (armstrong) where

import Data.Char (digitToInt)

armstrong :: Integral a => a -> Bool
armstrong n = let i = fromIntegral n
              in i == strong i

digits :: Int -> [Int]
digits = map digitToInt . show

strong :: Int -> Int
strong n = let l = digits n
               p = length l
           in
             sum $ map (^p) l
