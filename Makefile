.PHONY: up run-migrations

up:
	@echo "Starting up..."
	. venv/bin/activate ;\
		python manage.py runserver 0.0.0.0:8000

run-migrations:
	@echo "Running migrations..."
	. venv/bin/activate ;\
		python manage.py makemigrations api ;\
		python manage.py migrate
