

## For GitHub key setup
``` bash
git config --global user.email "[EMAIL]"
git config --global user.name "[NAME]"

ssh-keygen -t ed25519 -C "[EMAIL]"
cat ~/.ssh/id_ed25519.pub
```
[Copy and paste the publickey into GitHub](https://github.com/settings/keys)



## To make new projects
Make a project with the correct name on GitHub and then enter the following on the WSL terminal starting from a directory you want to make the new project in, e.g. 

``` bash
uv python install 3.12 --default

cd [DIRECTORY NAME e.g. ~/projects]
uv init [project-name]
cd [project-name]
uv add [packges]

git add *

git commit -m "[message]"
git branch -M main
git remote add origin git@github.com:[GITHUB PROJECT URL].git
git push -u origin main
```
