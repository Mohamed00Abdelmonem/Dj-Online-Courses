# Start Docker with Python 3.11
FROM python:3.11.6-slim-bullseye

# Set up Linux for Python
ENV PYTHONUNBUFFERED=1

# Update Linux kernel and install necessary tools
RUN apt-get update && apt-get -y install gcc libpq-dev

# Set the working directory in the container
WORKDIR /app

# copy & install requirements
COPY requirements.text /app/requirements.text


# install requirements
RUN pip install -r /app/requirements.text

# Copy the entire project folder
COPY ./ /app/