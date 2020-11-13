{-
My first haskell, project Euler problem 1
Meant to be executed in 
$ ghci
-}


import Data.List
import System.IO

target = 1000
multiples = sum [x | x <- [1..(target-1)], x `mod` 3 == 0 || x `mod`5 == 0]
