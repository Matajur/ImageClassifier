# Docker-command FROM specifies the base image of the container
# Base image is Linux with python-3.10 preinstalled
FROM python:3.10

ENV \
    PYTHONBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_CREATE="false"

RUN pip install "poetry==$POETRY_VERSION" 

# Environment variable
ENV APP_HOME /app

# Working directory inside the container
WORKDIR $APP_HOME

COPY poetry.lock $APP_HOME/poetry.lock
COPY pyproject.toml $APP_HOME/pyproject.toml

# Install the dependencies inside the container
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main

# Copy the other files to the working directory of the container
COPY . .

WORKDIR /app

# Port where the program is running inside the container
EXPOSE 8000

# Run the program inside the container
CMD ["python", "./Vision/manage.py", "runserver", "0.0.0.0:8000"]