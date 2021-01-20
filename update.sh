#!/bin/sh

# Stop the container, then delete the container and image.
stopDocker() {
    docker container kill darkspacebot
    docker container rm darkspacebot
    docker images rmi darkspace
}

# Build the image, start the container.
startDocker() {
    docker build -t darkspace .
    docker run -d --name darkspacebot darkspace
}

git fetch;
LOCAL=$(git rev-parse HEAD);
REMOTE=$(git rev-parse @{u});

# Update bot if local head differs from remote head.
if [ $LOCAL != $REMOTE ]; then
    stopDocker
    git pull origin master
    startDocker
    echo "Bot updated from GitHub"
else
    echo "Bot up to date!"
fi
