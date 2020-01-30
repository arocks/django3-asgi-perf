FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

RUN python -m pip install --upgrade pip

# install our dependencies
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt --no-cache-dir

# Copy project files
COPY . .

# Change to the directory containing manage.py for running Django commands easily
WORKDIR /opt/services/djangoapp/src/djangoapp
