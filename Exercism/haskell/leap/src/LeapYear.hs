module LeapYear (isLeapYear) where

(%%) :: Integer -> Integer -> Bool
(%%) a b = a `mod` b == 0

isLeapYear :: Integer -> Bool
isLeapYear year
  | year %% 400 = True
  | year %% 100 = False
  | year %% 4 = True
  | otherwise = False
