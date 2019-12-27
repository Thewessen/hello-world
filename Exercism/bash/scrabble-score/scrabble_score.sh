#!/usr/bin/env bash

set -o errexit
set -o nounset

declare -i score=0

for ((i = 0; i < ${#1}; i += 1)); do
  letter=${1:i:1}
  case ${letter^^} in
    [AEIOULNRST])
      score+=1
      ;;
    [DG])
      score+=2
      ;;
    [BCMP])
      score+=3
      ;;
    [FHVWY])
      score+=4
      ;;
    [K])
      score+=5
      ;;
    [JX])
      score+=8
      ;;
    [QZ])
      score+=10
      ;;
    *)
      score+=0
      ;;
  esac
done

echo $score
