#!/usr/bin/env bash


while read l; do
  dig +dnssec $l IN DS
done <top-dnssec-domains.txt
