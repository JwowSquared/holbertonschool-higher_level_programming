#!/bin/bash
# curls the address, returns available methods
curl -sI $1 | awk "NR==4" | cut -c 8-
