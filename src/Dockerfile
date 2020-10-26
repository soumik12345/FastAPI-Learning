# Pull Base Image
FROM python:3.8.1-alpine

# Set Working Directory
RUN mkdir /usr/src/backend
WORKDIR /usr/src/backend

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt
COPY ./requirements.txt /usr/src/backend/requirements.txt

# Install Dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev

# Install Python Dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /usr/src/backend/requirements.txt

# Remove pip cache
RUN rm -rf /root/.cache/pip

# Copy Project to Working Directory
COPY . /usr/src/backend/
