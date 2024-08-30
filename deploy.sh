#!/bin/bash
cd ~/nicksiv.github.io
rsync -av --delete ~/Documents/site/pub/ ~/nicksiv.github.io/site ;
#pub only customizations
echo ".prive{visibility:hidden;}" >> ~/nicksiv.github.io/site/style.css

# If a command fails then the deploy stops
set -e
printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
git push 
