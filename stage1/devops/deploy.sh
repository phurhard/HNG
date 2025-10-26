#!/bin/bash

# This is a script to deploy an application on a server

# it contains the following sections
# 1. Setup: which setups the server
# 2. Deployment: Deploying the application
# 3. Configuration: Configuring the server for the application and logging.

# part 1: functions
# collect user inputs


while getopts "g:p:b:s:" opt; do
    case $opt in
        g) gh_repo="$OPTARG" ;;
        p) pat="$OPTARG" ;;
        b) branch="$OPTARG" ;;
        s) ssh="$OPTARG" ;;
        *) echo "Usage $0 -g github-repo URL -p PAT -b Branch -s SSH values (ssh -i path/to/ssh-key username@server-ip" >&2; exit 1 ;;
    esac
done

# read -p "Enter repo: " gh_repo
echo "github repo: $gh_repo :: $pat :: $branch :: $ssh"
