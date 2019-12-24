#!/usr/bin/env bash

set -o errexit
set -o nounset

main() {
  result=''
  (( $1 % 3 == 0 )) && result+="Pling"
  (( $1 % 5 == 0 )) && result+="Plang"
  (( $1 % 7 == 0 )) && result+="Plong"

  echo ${result:-$1}
}

main "$@"
