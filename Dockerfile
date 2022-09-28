#to setting the docker image 
FROM python:3.11-rc-buster

WORKDIR /opt/

# Copy project
COPY . /opt/
RUN pip3 install -r requirements.txt
RUN chmod +x exec.sh
