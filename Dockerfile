# specifies which build engine used to build the image
FROM python:3.6

# specifies a working directory for our source code
WORKDIR /app

# copies your source code files
COPY . /app

# command executed to install dependencies
RUN pip install -r requirements.txt

# specifies a port number for our image to run in a docker container
EXPOSE 8080

# command to run our docker image in container
CMD ["python", "app.py"]
