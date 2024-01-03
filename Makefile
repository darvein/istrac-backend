.PHONY: build run

up:
	@echo "Starting up..."
	#python manage.py startapp istrac
	python manage.py runserver

run-migrations:
	@echo "Running migrations..."
	. venv/bin/activate ;\
		python manage.py makemigrations api ;\
		python manage.py migrate
