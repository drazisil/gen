run:
	python manage.py runserver 0.0.0.0:8000 --settings=gen.local_settings

dep:
	npm ci
	pipenv install

.PHONY: dep run