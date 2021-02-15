#!/bin/bash
# Finds and kills any processes that have the substring 'calc' in their names
# Use this if any weird error occurs
# Source: https://stackoverflow.com/questions/3510673/find-and-kill-a-process-in-one-line-using-bash-and-regex/3510850
kill $(ps aux | grep '[c]alc' | awk '{print $2}')
