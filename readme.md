Project of the Django2 Introduction from [Alura Courses](https://www.alura.com.br/).
This course is presented on a MacOS but i followed it using a ubuntu 18.04. All the adaptation are listed on the Install section.

---
### Install and Start your own Project

#### Create the repository project
```
mkdir DjangoProject
cd DjangoProject
```

#### Install python and venv
```
sudo apt install python3.7 
sudo apt install python3.7 python3-venv python3.7-venv
python3.7 -m venv py37-venv
```
To activate the virtual environment run: `source ./py37-venv/bin/activate`

For any package we will install we should use the virtual environment

#### Install Django latest
```
pip install django
pip install --upgrade pip
```
To check the version of packages installed run:  `pip freeze`

To check thecommands django allows run: `django-admin help`

To start the project the django project run: `django-admin startproject <project_name> <path_to_folder>` \
but in our case we created a project with name "alurareceita" on the current DjangoProject folder with the command: `django-admin startproject alurareceita . `

To check all the possible commands of the django project run: `python manage.py help` \
but to run the project we can use: `python manage.py runserver`

---

#### Installing Postgresql on Ubuntu 18.04

To install the postgresql run: ```sudo apt-get install postgresql``` and will show the packages installed like: 
```
 The following additional packages will be installed:
  libpq5 postgresql-10 postgresql-client-10 postgresql-client-common postgresql-common sysstat
 Suggested packages:
  postgresql-doc locales-all postgresql-doc-10 libjson-perl isag
 The following NEW packages will be installed:
  libpq5 postgresql postgresql-10 postgresql-client-10 postgresql-client-common postgresql-common sysstat
```
#### I found some hints here: https://tecadmin.net/install-postgresql-server-on-ubuntu/
#### to enter the postgresql menu with the generic postgres user:
* sudo su - postgres
#### using psql, the command-line interface to PostgreSQL.
* psql
* CREATE ROLE your_username WITH LOGIN CREATEDB ENCRYPTED PASSWORD 'your_password';
* \q
* su - your_username
* createdb my_db

---

### Installing python-dev for psutil problems
There is a [problem](https://github.com/giampaolo/psutil/issues/1143) with psutil that we will need the python-dev version to install its binaries, so we need the python-dev version of ourvirtual env. this will avoid problems on the installation of **pgAdmin4** and **psycopg2**

```
sudo apt-get install python3.7-dev
```


#### Installing psycopg2

In order to install psypg2 on the virtual env we must install libpq: ```sudo apt install libpq-dev```
```
pip install psycopg2-binary
pip install psycopg2
```

---

#### Installing pgAdmin4 (optional)

Install for https://www.pgadmin.org/download/pgadmin-4-python-wheel/ I download the pgadmin4-4.18-py2.py3-none-any.whl
```
pip3 install ./pgadmin4-4.18-py2.py3-none-any.whl 
nano py37-venv/lib/python3.7/site-packages/pgadmin4/config_local.py
```
Edit the config_local.py to adapt pgadmin4
```
import os
SERVER_MODE = False
DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
```
You can active pgAdmin4 running:  ```python py37-venv/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py``` and checking ```127.0.0.1:5050``` on your browser.

Some tutorial we followed: [medium](https://medium.com/@nikhilkrishnan/how-to-install-pgadmin4-in-ubuntu-16-04-with-python3-aecc79de4b7d) 
[howtoforge](https://www.howtoforge.com/tutorial/how-to-install-postgresql-and-pgadmin4-on-ubuntu-1804-lts/) 
[github-example](https://gist.github.com/rubinhozzz/368176fec80edcf449a76e15164ff728) 

Pgadmin4 uses flask to run on the browser and some libraries like flask_wtf uses the url_encode which currently is not [compatible](https://github.com/lepture/flask-wtf/commit/8b028994b68f5fffbf920770a0b4943a5225b282) with python3. After taking a look at [this](https://github.com/scoringengine/scoringengine/issues/670), in order to avoid that problem we followed applied this[change](https://techoverflow.net/2015/02/08/fixing-importerror-cannot-import-name-urlencode-in-python3/) 
on the files: \
py37-venv/lib/python3.7/site-packages/flask_wtf/recaptcha/widgets.py \
py37-venv/lib/python3.7/site-packages/flask_wtf/recaptcha/validators.py \
```
from werkzeug import url_encode
```
Change it for:
```
try:
    from werkzeug import url_encode
except ImportError:
    # Python 3
    from werkzeug.urls import url_encode
```

---

#### Extra steps for pageAdmin4, creating a script to trigger it
```
deactivate
touch ~/py37-venv/pgadmin4.sh
nano ~/py37-venv/pgadmin4.sh
```
And write the content as:
```
#!/usr/bin/env bash
source $(pwd)/py37-venv/bin/activate
python $(pwd)/py37-venv/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py
```
Then create a shortcut command for the pgadmin4: ```nano ~/.bashrc``` and edit/add the line ```alias pgadmin4='~/py37-venv-pgadmin/pgadmin4.sh'```


#### CREATING A NEW APP WITH STATIC FILES: 
#### run python manage.py startapp receitas
#### edit aulareceitas/settings.py -> INSTALLED_APPS
#### add receitas/urls.py -> urlpatterns = [ path() ]
#### edit receitas/views.py -> def function called on path
#### edit alurareceitas/urls.py -> path(, include('receitas.urls.py'))
#### add receitas/templates -> create html files using {% load static %}
#### add aulareceitas/static folder to be a reference for all static files
#### edit aulareceitas/settings.py -> STATIC_URL
#### edit aulareceitas/settings.py -> STATIC_ROOT
#### edit aulareceitas/settings.py -> STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'alurareceita/static'), ]
#### run python manage.py collectstatic -> generate ./static

#### add receitas/templates/base.html use {% load static %} and on body uses {% block content %} {% endblock %}
#### add receitas/templates/index.html -> index.html {% extends 'base.html' %} {% load static %} {% block content%}
#### add receitas/templates/partials -> creating header.html, footer.html use header and footer from index.html
#### add receitas/templatesindex.html uses {% include 'partials/header.html' %} {% include 'partials/footer.html' %}
