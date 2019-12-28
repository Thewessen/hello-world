#!/usr/bin/env bash

set -o errexit
# set -o nounset

if [[ $1 != "total" ]] && (( $1 < 1 )) || (( $1 > 64 )) || (( $# != 1 )); then
  echo "Error: invalid input" 
  exit 1
fi

if [[ $1 == "total" ]]; then
  grains=0
  for ((i = 0; i < 64; i += 1)); do
    grains=$( bc <<< "$grains + 2 ^ $i")
  done
  echo $grains
  exit 0
fi

bc <<< "2 ^ ($1 - 1)"
exit 0

