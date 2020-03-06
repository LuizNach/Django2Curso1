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
# some hints here: https://tecadmin.net/install-postgresql-server-on-ubuntu/
# to enter the postgresql menu:
* sudo su - postgres
# using psql, the command-line interface to PostgreSQL.
* psql