run:
	python manage.py runserver 0.0.0.0:8000 --settings=gen.local_settings

dep:
	npm ci
	pipenv install

test_dev:
	pipenv run coverage run manage.py test --settings=gen.local_settings
	pipenv run coverage xml


test:
	pipenv run coverage run manage.py test
	pipenv run coverage xml

.PHONY: dep run test test_dev
