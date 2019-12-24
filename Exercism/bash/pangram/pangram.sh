#!/usr/bin/env bash

set -o errexit
set -o nounset

declare lowercase=${1,,}
declare sanitized=${lowercase//[^a-zA-Z]}

for letter in {a..z}; do
  if [[ $sanitized != *$letter* ]]; then
    echo false
    exit 0
  fi
done

echo true
exit 0
