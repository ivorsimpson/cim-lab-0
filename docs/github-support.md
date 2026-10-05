

## For GitHub key setup (keys needs to be placed in ~/.ssh, best to stick with the default location/filename)
``` bash
git config --global user.email "[EMAIL]"
git config --global user.name "[NAME]"

ssh-keygen -t ed25519 -C "[EMAIL]"
cat ~/.ssh/id_ed25519.pub
```
[Copy and paste the publickey into GitHub](https://github.com/settings/keys)


**Make sure you make a copy of your private and public keys for future use**
If you're copying some keys you already have, put them in .ssh and type the following the start the ssh agent and make it aware of your private keys
```bash
eval "$(ssh-agent -s)" 
ssh-add ~/.ssh/[keyname, e.g. id_ed25519]
```

Check your keys work!
```bash
ssh -T git@github.com
```

**Note: If you reinstantiate the WSL environment the `eval "$(ssh-agent -s)" ` and the key adding `ssh-add ~/.ssh/[keyname, e.g. id_ed25519]`  needs to be run again. Otherwise the machine won't be able to authenticate itself with Github.** If you get access denied, that is the most likely culprit. 


## If you want to copy a repository within GitHub you can make a "Fork" of it to your user, and then follow the instruction below for working from that

## Starting from an existing repository
``` bash
cd [DIRECTORY NAME e.g. ~/projects]
git clone git@github.com:[GITHUB PROJECT URL].git
cd [project-name]
uv sync
```

## If you want to push a version of a repository that you have cloned, to your GitHub, you need to make a new empty repository on GitHub and perform the following steps
```bash
cd [repo name]
git remote remove origin
git remote add origin git@github.com:[your username]/[your repo name].git
git branch -M main
git push -u origin main
```


## To make new projects from scratch
Make a repostiory with the correct name on GitHub and then enter the following on the WSL terminal starting from a directory you want to make the new project in, e.g. 

``` bash
cd [DIRECTORY NAME e.g. ~/projects]
git clone git@github.com:[GITHUB PROJECT URL].git
cd [project-name]
uv init [project-name]
uv python install 3.12
uv add [python packges]

# When you've got your code ready
git add [filenames or *]

git commit -m "[message]"
git push -u origin main
```
