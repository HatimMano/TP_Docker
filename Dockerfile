FROM python:3.9

RUN apt update
RUN apt install python3

# set the working directory in the container
WORKDIR /Users/hatimmanowaraly/Desktop/EFREIM1/DevOps/tp1

COPY weather.py ./

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python3", "./weather.py" ]
