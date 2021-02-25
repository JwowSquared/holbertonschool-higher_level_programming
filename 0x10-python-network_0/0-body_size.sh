#!/usr/bin/bash
# curls the address and counts the amount of chars
curl -s $1 | wc -m
