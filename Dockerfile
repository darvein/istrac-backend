FROM python:3.11-slim

# Set environment variables to ensure that Python runs in unbuffered mode, which is recommended when running Python within Docker containers
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
