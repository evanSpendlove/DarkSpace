#!/bin/sh

f_flag=false

print_usage() {
  printf "Usage: stop <-f>\n"
}

while getopts 'f' flag; do
  case "${flag}" in
    f) f_flag=true ;;
    *) print_usage
       exit 1 ;;
  esac
done

# Stop the container
docker container kill darkspacebot

# Remove the container if the argument is specified
if [ "$f_flag" = true ] ; then
    docker container rm darkspacebot
fi
