#!/bin/bash

export MY_IP=$(hostname --all-ip-addresses | cut -d' ' -f1)
export ROS_MASTER_URI=http://$MY_IP:11311
export ROS_IP=$MY_IP

docker-compose up --force-recreate
