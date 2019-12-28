#!/usr/bin/env bash

set -o errexit
set -o nounset

declare -i sum_of_squares=0
declare -i square_of_sum=0

for ((i = 1; i <= $2; i += 1)); do
  sum_of_squares+=`bc <<< "$i ^ 2"`
  square_of_sum+="$i"
done

case $1 in
  sum_of_squares)
    echo $sum_of_squares
    exit 0
    ;;
  square_of_sum)
    bc <<< "$square_of_sum ^ 2"
    exit 0
    ;;
  difference)
    bc <<< "$square_of_sum ^ 2 - $sum_of_squares"
    exit 0
    ;;
  *)
    exit 1
esac
