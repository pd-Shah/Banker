#!/bin/bash

input="$1"

if [ "$input" = "development" ]; then
  echo "develpment mode..." &&
    echo "DO NOT USE IN ANY SERVER" &&
    echo "PROJECT ROOT DIR:" &&
    echo $(pwd) &&
    cp configs/docker-compose-staging.conf docker-compose.yml &&
    echo "DONE"
elif [ "$input" = "testing" ]; then
  echo "...under consternation..."
else
  echo "...production is under consternation..."
fi

sudo docker-compose build &&
  sudo docker-compose up --remove-orphans
