# Use an official Python runtime as a parent image
FROM python:3.5-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#pre-reqs for psycopg2
RUN apk update && \
    apk add bash && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Export flask app
ENV FLASK_APP debateit.py

# Run debateit.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]