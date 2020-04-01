#!/bin/bash

pwd=$(pwd)
question="Are you sure you want to delete the content in this directory (${pwd}) [yY]?"
echo $question
read -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
   rm -r log input output plots old_logs
   rm *.pickle
fi
