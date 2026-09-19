# 🟩 GitHub Green Square Experiment (For Fun)

This repository contains a Python script created as a fun programming experiment to understand and manipulate Git's native environment variables (`GIT_COMMITTER_DATE` and `GIT_AUTHOR_DATE`). 

### 🤔 What does this do?
The script automates the process of backdating empty commits over the past 365 days. It was built purely for **educational and entertainment purposes** to see how Git history handles retroactive timestamp overrides on the GitHub contribution graph.

### 🛠️ Script Overview
The Python code loops through the last 365 days, modifies the internal author dates, and commits an empty change 4 times per day to generate the green activity chart. 
