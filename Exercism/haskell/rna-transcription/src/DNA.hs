module DNA (toRNA) where

toRNA :: String -> Either Char String
toRNA = traverse transcribe

transcribe :: Char -> Either Char Char
transcribe 'C' = Right 'G'
transcribe 'G' = Right 'C'
transcribe 'T' = Right 'A'
transcribe 'A' = Right 'U'
transcribe x = Left x
