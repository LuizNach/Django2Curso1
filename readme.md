# install python and venv
* sudo apt install python3.7
* sudo apt install python3.7 python3-venv python3.7-venv
* python3.7 -m venv py37-venv
* source ./py37-venv/bin/activate

* pip install django
* pip install --upgrade pip
* pip freeze

* django-admin help
* django-admin startproject alurareceita .
* python manage.py help

# CREATING A NEW APP WITH STATIC FILES: 
# run python manage.py startapp receitas
# edit aulareceitas/settings.py -> INSTALLED_APPS
# add receitas/urls.py -> urlpatterns = [ path() ]
# edit receitas/views.py -> def function called on path
# edit alurareceitas/urls.py -> path(, include('receitas.urls.py'))
# add receitas/templates -> create html files using {% load static %}
# add aulareceitas/static folder to be a reference for all static files
# edit aulareceitas/settings.py -> STATIC_URL
# edit aulareceitas/settings.py -> STATIC_ROOT
# edit aulareceitas/settings.py -> STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'alurareceita/static'), ]
# run python manage.py collectstatic -> generate ./static

# add receitas/templates/base.html use {% load static %} and on body uses {% block content %} {% endblock %}
# add receitas/templates/index.html -> index.html {% extends 'base.html' %} {% load static %} {% block content%}
# add receitas/templates/partials -> creating header.html, footer.html use header and footer from index.html
# add receitas/templatesindex.html uses {% include 'partials/header.html' %} {% include 'partials/footer.html' %}


* sudo apt-get install postgresql
# The following additional packages will be installed:
#  libpq5 postgresql-10 postgresql-client-10 postgresql-client-common postgresql-common sysstat
# Suggested packages:
#  postgresql-doc locales-all postgresql-doc-10 libjson-perl isag
# The following NEW packages will be installed:
#  libpq5 postgresql postgresql-10 postgresql-client-10 postgresql-client-common postgresql-common sysstat
# I found some hints here: https://tecadmin.net/install-postgresql-server-on-ubuntu/
# to enter the postgresql menu with the generic postgres user:
* sudo su - postgres
# using psql, the command-line interface to PostgreSQL.
* psql
* CREATE ROLE your_username WITH LOGIN CREATEDB ENCRYPTED PASSWORD 'your_password';
* \q
* su - your_username
* createdb my_db

# Installing pgAdmin4
# Install for https://www.pgadmin.org/download/pgadmin-4-python-wheel/ I download the pgadmin4-4.18-py2.py3-none-any.whl

# There is a problem with psutil that we will need the python-dev version to install its binaries, so we need the python-dev version of ourvirtual env: https://github.com/giampaolo/psutil/issues/1143

* sudo apt-get install python3.7-dev
* pip3 install ./pgadmin4-4.18-py2.py3-none-any.whl 
* nano py37-venv/lib/python3.7/site-packages/pgadmin4/config_local.py
* python py37-venv/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py 
# This is the best tutorial: https://medium.com/@nikhilkrishnan/how-to-install-pgadmin4-in-ubuntu-16-04-with-python3-aecc79de4b7d
# https://www.howtoforge.com/tutorial/how-to-install-postgresql-and-pgadmin4-on-ubuntu-1804-lts/
# https://gist.github.com/rubinhozzz/368176fec80edcf449a76e15164ff728
# https://techoverflow.net/2015/02/08/fixing-importerror-cannot-import-name-urlencode-in-python3/
# I had some problems on flask_wtf/widget, flas_wtf/captcha for using python3 but a corrected doing this: 
# https://github.com/lepture/flask-wtf/commit/8b028994b68f5fffbf920770a0b4943a5225b282 after taking a look at this https://github.com/scoringengine/scoringengine/issues/670
# files paths: /py37-venv/lib/python3.7/site-packages/werkzeug/utils.py
