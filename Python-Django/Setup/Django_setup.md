Django 2.0 supports: python 3.4, 3.5, 3.6, 3.7


# Using Apple Macbook M1 for Python & Django based website development
(2021)
- https://medium.com/@suyashmohan/using-apple-macbook-m1-for-python-django-based-website-development-572bca04f5c3
# Your First Steps With Django: Set Up a Django Project (2021)
https://realpython.com/django-setup/


## Install Python and Django Dependencies
```sh
# use python installed through Xcode
xcode-select --install

# install HomeBrew (to help install libpq)
# follow instructions from https://brew.sh/
# install libpq
brew install libpq --build-from-source
```

## Create virtual environment
```sh
# upgrade pip
python3 -m pip install --upgrade pip
pip install --upgrade pip

# navigate to folder to set up new virtual env
cd desktop

# create new python virtual environment
python3 -m venv <name>
  python3 -m venv MyDjangoEnv
# activate virtual environment
source MyDjangoEnv/bin/activate # (MyDjangoEnv) enabled
deactivate
```

## Install Django into virtual environment
```sh
# install django into dedicated virtual env workspace
python3 -m pip install django
  python3 -m pip install django==2.2.11 # for spec version

# after django install, pin dependencies (req's file) for version tracking
python3 -m pip freeze > requirements.txt
pip freeze # asgiref==3.5.0 (async server gateway interface), Django==4.0.2, sqlparse==0.4.2

# if working on existing project/dependencies and req file, can install correct Django v w/ all other necessary packages using:
python -m pip install -r requirements.txt
```

## Set up Django Project
```sh
# create scaffolding for new web app
  # Django framework distinguishes between project and apps
    # Project: high-level unit organization containing logic for whole web app; each project can contain multiple apps
    # App: lower-level unit of web app; can have 0 to many apps in proj

# with (env) still activated
# create django project
django-admin startproject <project_name>
  django-admin startproject first_project
  django-admin startproject first_project . # . avoids creating top-level proj folder

```

- creates the following folder structure:
    first_project/ (top-level project folder)
    |── first_project/ (loser-level folder for mgmt app)
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py (proj command center; same as `django-admin` cmd-line util)


## Start Django App
```sh
cd first_project

# don't need to use `django-admin` anymore, can execute startapp cmd through manage.py instead
# generate default folder structure for Django app
python manage.py startapp <appname>
  python manage.py startapp first_app
```

- new app folder structure:
├── example_app/
│   │
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── __init__.py (python uses this file to declare folder as a package, allowing Django to use code from different apps)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py (declare app's models in this file, allowing Django to interface w/ DB of web app)
│   ├── tests.py
│   └── views.py (most of code logic of app is written in this file)



```sh

# cd to Django proj and install required dependencies
# set correct path for PostgreSQL and Open SSL header and library paths
export LDFLAGS="-L/opt/homebrew/opt/libpq/lib -L/opt/homebrew/opt/openssl@1.1/lib"
pip install -r requirements.txt





# runs python interpreter with all of Django project configs so you can execute cmds against DB or any other resources in Django project
  # in the shell, proj is not running as http service, but can perform operations like DB queries or calling internal functions
python3 manage.py shell

# run the server for django application
python3 manage.py runserver

# access server: http://127.0.0.1:8000/
# admin page: http://127.0.0.1:8000/admin

```





# Install Django on Mac with PIP and VirtualEnv (2014)
- https://www.youtube.com/watch?v=FshRArXrEcM

## Install Django in a virtual environment
```sh
python
exit()

sudo easy_install pip # pip - python package installer
# enter password
sudo pip install virtualenv

cd desktop
# install/create folder for new virtual environment
virtualenv somename
cd somename
ls # bin include lib

# activate (enter into) virtual environment
source bin/activate

# now in virtual environment: somename
  # indicated by (somename)$

# outputs package and version installed in current environment as config file that can be used with pip install -r
pip freeze # wsgiref==0.1.2 (web server gateway interface)
pip install django==1.4.5 # installs django w/ version
pip freeze # Django==1.4.5 wsgiref==0.1.2

# in new terminal (outside venv)
pip freeze # outputs everything installed for pip; Django==1.5.4
# close new terminal

pip install django --upgrade # updates to latest stable version
# will uninstall old version (1.4.5), and install 1.6.1

# can install a 2nd new virtual environment in same dir as 1st
cd desktop
virtualenv somename2 # will create new folder somename2
cd somename2
ls # bin, include lib
source bin/activate # activates venv somename2

# entered (somename2)
pip freeze # wsgiref=0.1.2
pip install django
pip freeze # Django==1.6.1 wsgiref=0.1.2

# start django project
django-admin startproject first_project
ls # bin, include, lib, first_project
cd first_project
ls # manage.py, first_project
python manage.py runserver
# open browser at default url http://127.0.0.1:8000/

```

## Install Django outside of virtual environment (globally)
```sh
# can use either:
sudo easy_install django
sudo pip install django==1.6.1 # for specific version
  sudo pip install django --upgrade # for latest stable version
# enter pw
```
