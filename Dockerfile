FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /weblopers_api

# Copy the current directory contents into the container at /app
COPY requirements.txt .

COPY . .
# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y libpq-dev
RUN pip install -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=weblopers_api.settings

# Expose port 8000 for the Django app to listen on
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]