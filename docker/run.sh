sudo chmod 777 /var/run/docker.sock
docker run --rm --shm-size 8G --gpus all -v $HOME:$HOME -it codetr:latest