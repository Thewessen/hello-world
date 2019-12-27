#!/usr/bin/env bash

set -o errexit
set -o nounset


if (( $# == 0 )) || [[ $1 =~ ^[[:space:]]*$ ]]; then
  echo 'Fine. Be that way!'
  exit 0
fi

sanitized=${1//[^a-zA-Z?]}
if [[ $sanitized =~ ^[A-Z]+\?$ ]]; then
  echo "Calm down, I know what I'm doing!"
  exit 0
elif [[ ${sanitized: -1} == "?" ]]; then
  echo 'Sure.'
  exit 0
elif [[ $sanitized =~ ^[A-Z]+$ ]]; then
  echo 'Whoa, chill out!'
  exit 0
else
  echo 'Whatever.'
  exit 0
fi
