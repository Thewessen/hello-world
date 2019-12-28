#!/usr/bin/env bash

for ((i = ${#1}; i > 0; i -= 1)); do
  printf "${1:$i-1:1}"
done
