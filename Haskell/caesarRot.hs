#!/usr/bin/ghci

shiftForwards :: Char -> Char
shiftForwards 'z' = 'a'
shiftForwards 'Z' = 'A'
shiftForwards c = succ c

shiftBackwards :: Char -> Char
shiftBackwards 'a' = 'z'
shiftBackwards 'A' = 'Z'
shiftBackwards c = pred c

caesarRot :: Int -> [Char] -> [Char]
caesarRot num str
        | num > 0 = caesarRot (num - 1) (map shiftForwards str) 
        | num < 0 = caesarRot (num + 1) (map shiftBackwards str) 
        | num == 0 = str

