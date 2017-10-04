### Python AWS EMR Status via Arduino LEDs

Initial python setup:

```bash
# install pip
sudo easy_install pip

# check pip version
pip --version
# pip 8.1.1 from /Library/Python/2.7/site-packages (python 2.7)

# upgrade to latest pip
sudo pip install --upgrade pip

# check pip version
pip --version
# pip 9.0.1 from /Library/Python/2.7/site-packages (python 2.7)

# (optional) fix six osx issue:
sudo pip install --ignore-installed six

# install virtualenvwrapper
sudo pip install virtualenvwrapper

# create virtual env for pip packages
mkvirtualenv -p /usr/bin/python2.7 emr_status

# use virtual env
workon emr_status

# install pip packages
pip install -r requirements.txt
```

Execute script:
```
python emr_status.py
```
