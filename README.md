# Python Bounce Project

This starter project is a single python script that runs out of the file bounce.py. It
creates an animation of a ball moving through a 2D space with matplotlib.

The project is already setup be run in one of two environments.

It can be run directly from a locally installed python environment, or it can be run within a
docker container. These two options are described below. You can choose whichever option works
better given your existing environment.


## 1. You will need a version of python that is 3.7 or higher with a version of the matplotlib
installed that is version 3.2 or higher.

If you simply run (from the working directory containing bounce.py)

```console
$ python bounce.py
```

You should see a matplotlib figure open, and the animation will play.


## 2. You will need docker setup and ready to run. If you already have a docker install you can
test it by running the following command


```console
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu console

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

### Running the script in a docker container

To run the script in a docker container, you will simply use our prebuilt image,
on dockerhub, bmilne/pybounce
(this image was built from the Dockerfile in this repo, if you are curious).
It has an install of python 3.11 with matplotlib 3.6.5.

The Linux command to run the bouncy.py script is shown below. You need to run it
from the directory that contains bounce.py
```console
$ docker run --rm -v `pwd`:"/bounce" bmilne/pybounce
```

The command line options are --rm (telling docker to clean up the container when it exits)
and the -v which mounts the current working directory as /bounce in the image.

The script will produce a movie file, "bounce_out.mp4" in the same directory, which you can
view with vlc or any other tool for viewing mp4's.


## 2b. How to install and setup docker.

If you want to install docker, get docker-ce (the community edition / OSS version of docker)
as described here:

https://docs.docker.com/install/

Then run the hello-world test describe in part 2.

If you are in a Linux environment, you may want to add your user to the "docker" group
so that you can run docker commands without SUDO. TO do this, and then _log out and log back in_:

```console
$  sudo usermod -aG docker $USER
```
