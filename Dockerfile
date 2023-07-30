# base image
FROM python:3.11-alpine

# set working directory
WORKDIR /app

# copy the dependencies file to the working directory
#COPY requirements.txt .

# install dependencies
RUN apk update && apk add --no-cache gcc musl-dev linux-headers

RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY app.py .

EXPOSE 5000

# command to run on container start
CMD [ "python", "./app.py" ]


#docker build -t my-flask-app .
#docker run -d -p 5000:5000 my-flask-app

