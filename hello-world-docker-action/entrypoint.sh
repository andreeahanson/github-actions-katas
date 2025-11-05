#!/bin/bash

greeting_type="$1"
who_to_greet="$2"

message="$greeting_type $who_to_greet"
echo "$message"

time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT
echo "message=$message" >> $GITHUB_OUTPUT
