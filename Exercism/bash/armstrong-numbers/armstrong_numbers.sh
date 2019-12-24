#!/usr/bin/env bash

set -o errexit
set -o nounset

main() {
  declare -i sum=0
  declare -i power=${#1}

  for ((i = 0; i <= $power; i += 1)); do
    declare -i digit=${1:i:1}
    sum+=$(( digit ** power ))
  done

  (( sum == $1 )) && echo true || echo false
}

main "$@"
