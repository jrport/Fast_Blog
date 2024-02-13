#! /usr/bin/bash

sudo docker ps -a && sudo docker images
 
sudo docker rm blog_app && sudo docker rmi blog_app
