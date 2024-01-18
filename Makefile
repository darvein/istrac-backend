.PHONY: up run-migrations

up:
	@echo "Starting up..."
	. venv/bin/activate ;\
		python manage.py runserver 0.0.0.0:8000
		#python manage.py collectstatic ;\

run-migrations:
	@echo "Running migrations..."
	. venv/bin/activate ;\
		python manage.py makemigrations api ;\
		python manage.py migrate

run-fixtures:
	@echo "Running fixtures..."
	. venv/bin/activate ;\
		python manage.py loaddata api/fixtures/categories.yaml
		python manage.py loaddata api/fixtures/locations.yaml
		python manage.py loaddata api/fixtures/tplaces.yaml
