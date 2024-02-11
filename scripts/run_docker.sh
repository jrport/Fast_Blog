#! /usr/bin/bash

# First build the docker image
docker build --tag blog_app .

# Then create its container
docker run --name blog_app -d -p 80:80 blog_app
