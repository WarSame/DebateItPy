# Use an official Python runtime as a parent image
FROM python:3.6-alpine

# Set the working directory to /server
WORKDIR /server

# Copy the current directory contents into the container at /server
ADD . /server

#pre-reqs for psycopg2
RUN apk update && \
    apk add bash && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Export flask app
ENV FLASK_APP debateit.py
ENV DATABASE_URI postgresql://pguser:pguser@db:5432/debateit
ENV SECRET_KEY somesecretkey
ENV GOOGLE_LOGIN_CLIENT_ID 353296250090-qujtgp93p1sl7v3gc72u9kh84q3t1ntf.apps.googleusercontent.com
ENV GOOGLE_LOGIN_CLIENT_SECRET uzEFi2y3rlt2BqsArNXKHG9c
ENV FACEBOOK_LOGIN_CLIENT_ID 485484021845294
ENV FACEBOOK_LOGIN_CLIENT_SECRET this

# Run server.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
