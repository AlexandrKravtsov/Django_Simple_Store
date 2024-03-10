install-django:
	pip install django

startproject:
	python -m django startproject settings

runserver:
	python manage.py startapp

startapp:
	python manage.py startapp animals


makemigrations:
	python manage.py makemigrations blog

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

fill_db:
	python manage.py fill_db

shell:
	python manage.py shell