#!/bin/bash

branch="$(git branch --show-current)"

if [[ -z "$branch" ]]; then
  echo "Not on a branch (detached HEAD). Aborting."
  exit 1
fi

git fetch origin "$branch"

git status

# Show the last 10 commits
git log -"%s" --date=format:"%Y-%m-%d %H:%M:%S" -15

sleep 2

git diff --cached

git add .

# Only push if the commit was successful
if git commit; then
  echo "Commit successful. Pushing to origin..."
  git push -u origin "$branch"
else
  echo "Commit was aborted or failed. Push canceled."
  exit 1
fi

# Log the last 999 commits with their messages and full bodies into z.txt
git log -999 --format="%s%n%n%b" > z.txt
