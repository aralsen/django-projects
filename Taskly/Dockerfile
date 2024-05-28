# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

# Copy the current directory contents into the container at /Taskly
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]