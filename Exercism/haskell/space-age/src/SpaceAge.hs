module SpaceAge (Planet(..), ageOn) where

data Planet = Mercury
            | Venus
            | Earth
            | Mars
            | Jupiter
            | Saturn
            | Uranus
            | Neptune

orbit :: Float -> Float -> Float
orbit = flip (/) . (*31557600.0)

ageOn :: Planet -> Float -> Float
ageOn Mercury = orbit 0.2408467
ageOn Venus = orbit 0.61519726
ageOn Earth = orbit 1.0
ageOn Mars = orbit 1.8808158
ageOn Jupiter = orbit 11.862615
ageOn Saturn = orbit 29.447498
ageOn Uranus = orbit 84.016846
ageOn Neptune = orbit 164.79132
