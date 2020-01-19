module Bob (responseFor) where

import Data.Char

responseFor :: String -> String
responseFor xs
  | isSilent xs                    = "Fine. Be that way!"
  | (isQuestion xs) && (isYell xs) = "Calm down, I know what I'm doing!"
  | isYell xs                      = "Whoa, chill out!"
  | isQuestion xs                  = "Sure."
  | otherwise                      = "Whatever."


isSilent :: String -> Bool
isSilent = all isSpace

isQuestion :: String -> Bool
isQuestion = (== '?') . last . filter (/= ' ')

isYell :: String -> Bool
isYell say
  | any isLower say = False
  | any isUpper say = True
  | otherwise = False
