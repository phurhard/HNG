#!/bin/bash

# This is a script to deploy an application on a server

# it contains the following sections
# 1. Setup: which setups the server
# 2. Deployment: Deploying the application
# 3. Configuration: Configuring the server for the application and logging.

# part 1: functions
# collect user inputs

github-repo = read "your github name"
echo $github-repo
while getopts "g:p:b:s" opt; do
    case $opt in
        g) gh-repo="$OPTARG" ;;
        p) pat=$"OPTARG" ;;
        b) branch="$OPTARG" ;;
        s) ssh="$OPTARG" ;;
        *) echo "Usage $0 -g github-repo URL -p PAT -b Branch -s SSH values (ssh -i path/to/ssh-key username@server-ip" >&2; exit 1 ;;
    esac
done

echo "github repo: $gh-repo"
