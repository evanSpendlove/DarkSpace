#!/bin/sh

if docker images | grep "darkspace"
then
    if docker container ls -a | grep "darkspacebot" ; then
        docker container start darkspacebot
    else
        docker run -d --name darkspacebot darkspace
    fi
else
    docker build -t darkspace . && docker run -d --name darkspacebot darkspace
fi
