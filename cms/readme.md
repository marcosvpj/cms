
```console
git clone
python -m venv .cms
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```