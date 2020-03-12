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


#### Installing Postgresql on Ubuntu 18.04

* sudo apt-get install postgresql
#### The following additional packages will be installed:
####  libpq5 postgresql-10 postgresql-client-10 postgresql-client-common postgresql-common sysstat
#### Suggested packages:
####  postgresql-doc locales-all postgresql-doc-10 libjson-perl isag
#### The following NEW packages will be installed:
####  libpq5 postgresql postgresql-10 postgresql-client-10 postgresql-client-common postgresql-common sysstat
#### I found some hints here: https://tecadmin.net/install-postgresql-server-on-ubuntu/
#### to enter the postgresql menu with the generic postgres user:
* sudo su - postgres
#### using psql, the command-line interface to PostgreSQL.
* psql
* CREATE ROLE your_username WITH LOGIN CREATEDB ENCRYPTED PASSWORD 'your_password';
* \q
* su - your_username
* createdb my_db


### Installing python-dev for psutil problems
There is a [problem](https://github.com/giampaolo/psutil/issues/1143) with psutil that we will need the python-dev version to install its binaries, so we need the python-dev version of ourvirtual env. this will avoid problems on the installation of **pgAdmin4** and **psycopg2**

```
sudo apt-get install python3.7-dev
```


#### Installing pgAdmin4
#### Install for https://www.pgadmin.org/download/pgadmin-4-python-wheel/ I download the pgadmin4-4.18-py2.py3-none-any.whl
* pip3 install ./pgadmin4-4.18-py2.py3-none-any.whl 
* nano py37-venv/lib/python3.7/site-packages/pgadmin4/config_local.py
* python py37-venv/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py 
#### This is the best tutorial: https://medium.com/@nikhilkrishnan/how-to-install-pgadmin4-in-ubuntu-16-04-with-python3-aecc79de4b7d
#### https://www.howtoforge.com/tutorial/how-to-install-postgresql-and-pgadmin4-on-ubuntu-1804-lts/
#### https://gist.github.com/rubinhozzz/368176fec80edcf449a76e15164ff728
#### https://techoverflow.net/2015/02/08/fixing-importerror-cannot-import-name-urlencode-in-python3/
#### I had some problems on flask_wtf/widget, flas_wtf/captcha for using python3 but a corrected doing this: 
#### https://github.com/lepture/flask-wtf/commit/8b028994b68f5fffbf920770a0b4943a5225b282 after taking a look at this https://github.com/scoringengine/scoringengine/issues/670
#### files paths: /py37-venv/lib/python3.7/site-packages/werkzeug/utils.py


#### Extra stepsfor pageAdmin4, creating a script to trigger it
deactivate
touch ~/py37-venv/pgadmin4.sh
nano ~/py37-venv/pgadmin4.sh
#### and write the content as:
#!/usr/bin/env bash
source $(pwd)/py37-venv/bin/activate
python $(pwd)/py37-venv/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py

#### Installing psycopg2
* sudo apt install libpq-dev
* pip install psycopg2-binary
* pip install psycopg2