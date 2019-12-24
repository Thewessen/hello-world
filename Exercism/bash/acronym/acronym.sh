#!/usr/bin/env bash

set -o errexit
set -o nounset

for word in ${1//[-_*]/ }; do
  first_chr=${word::1}
  printf ${first_chr^^}
done
