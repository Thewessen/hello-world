module Pangram (isPangram) where

import Data.Char

isPangram :: [Char] -> Bool
isPangram = flip all ['a'..'z'] . flip elem . map toLower
