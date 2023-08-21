# Day 70: Git, Github, and Version Control

## Overview

- Topics: Git, Github, and Version Control 

### The challenge

 

### Links

- Solution URL: [Git, Github, and Version Control](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day70)

### Built with



### References
- [Github GitIgnore](github.com/gitHub/gitignore) a repository owned by the GitHub team for Git Ignore, which is a pre-made collection of useful git ignore templates.
- [Beginner Friendly Repos](https://github.com/MunGell/awesome-for-beginners)
- [Wordle Game Repo](https://github.com/ritik48/Wordle-Game)
- [Git Exercises](https://learngitbranching.js.org/) Complete the challenges here to dive deeper into Git, including learning about Cherry-Picking, Git Rebase, and more. 

### Notes
Git Commands (Windows)
- ```git status```
- ```git init```
- ```git add .```
- ```git commit -m```
- ```git push```  Pushes to github
- ```git push origin main -u```  Pushes to github
- ```git rm --cached -r .```  Use this to remove files from my staging area / undo the last step. 
- ```git log```  This lets you see what commits you have made
- ```clear``` (to clear terminal)
- To exit the “git log” operation, press the “q” key

Create Remote Repository
- ```git remote add <name> <url>```
- ```git push -u <remote name>  <branch name>```  Pushes local repository to the remote repository. 

To Create a file:
- ```touch name-of-file.filetype```

To Create a GitIgnore File:
- ```touch .gitignore```
- ```code .gitignore```  (Open GitIgnore for Windows)

To Clone a repository
  - ```git clone url```

To Create a BRANCH
- git branch name-of-branch
- git branch (Use this to see which branch you are on)

TO MERGE the branches
- git merge name-of-branch
- Steps:
1. Go back to the main branch
git checkout main
2. Merge
git merge name-of-branch
Note: if VIM comes out, type ```:q!```  (to save and quit)

To SWITCH to BRANCH
- git checkout name-of-branch