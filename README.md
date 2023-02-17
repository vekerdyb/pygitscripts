# pygitscripts
Git helper scripts I use

With `fish` shell I use this roughly as: 

```fish
git clone git@github.com:vekerdyb/pygitscripts.git
cd pygitscripts

# if you use virtualenvwrapper / virtualfish:
mkvirtualenv pygitscripts 
# otherwise:
python -m venv venv
source venv/bin/activate.fish

pip install -r requirements.txt

set PYTHON_BINARY (which python)
alias cb "$PYTHON_BINARY $PWD/git-change-branch.py"
alias fixupa "$PYTHON_BINARY $PWD/git-fixup.py --add-all"
alias fixup "$PYTHON_BINARY $PWD/git-fixup.py"
eval fish
```

Haven't tested with other shells yet.

I assume it would be something like this for zsh:
```zsh
git clone git@github.com:vekerdyb/pygitscripts.git
cd pygitscripts

# if you use virtualenvwrapper / virtualfish:
mkvirtualenv pygitscripts 
# otherwise:
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
alias cb="$(which python) $(pwd)/git-change-branch.py"
alias fixupa="$(which python) $(pwd)/git-fixup.py --add-all"
alias fixup="$(which python) $(pwd)/git-fixup.py"
eval zsh
```