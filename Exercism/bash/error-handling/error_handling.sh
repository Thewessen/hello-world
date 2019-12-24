#!/usr/bin/env bash

set -o errexit
set -o nounset

main () {
  if (( $# != 1 )); then
    echo "Usage: ./${0%.*} <greetee>"
    exit 1
  fi

  echo "Hello, $1"
}

main "$@"
