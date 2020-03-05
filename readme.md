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
* python manage.py startapp receitas

# edit aulareceitas/settings.py -> INSTALLED_APPS
# edit receitas/urls.py
# edit receitas/views.py
# edit alurareceitas/urls.py