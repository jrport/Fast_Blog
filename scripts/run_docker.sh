#! /usr/bin/bash

# First build the docker image
sudo docker build --tag blog_app .

# Then create its container
sudo docker run --name blog_app -d -i --tty -p 80:80 blog_app
