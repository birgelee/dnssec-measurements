#!/usr/bin/env bash


while read l; do
  dig +dnssec a.$l IN CAA
done <top-dnssec-domains.txt
