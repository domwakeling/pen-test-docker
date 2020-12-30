# Introduction

This repository implements the tools described in HackerSploit's '[Python
3 for Pentesting](https://www.youtube.com/watch?v=UadqiHXfvsg&list=PLBf0hzazHTGM_dncTqO9l-0zUQYP0nNPU)'
course. Parts of that course are also on the FreecodeCamp syllabus.

But to add a wrinkle, and learn/reinforce another new skill, I am also going to try to
'Docker-ise' everything.

## Index
**[Building the Docker image](#building-the-docker-image)**

**[Included Tools](#included-tools)**
* **[TCP Server and Client](#tcp-server-and-client)**
  * [TCPserver](#1.-tcpserver)
  * [TCPclient](#2.-tcpclient)
  * [Example - Running Docker-ised](#example---running-docker-ised)
  * [Example - Docker-ised server](#example---docker-ised-server)
* **[Scanner](#scanner)**
  * [Running Locally](#running-locally)

**[Notes](#notes)**

## Building the Docker image

*The image will evenutally be available on Docker Hub as* `domwakeling/pen-test`.

To build the Docker image, you need to be at the root file of the code (the one where the `Dockerfile`
sits), **not** at the `src` folder.

Run the following command to build:

`docker build -t pen-test .`

**Following instruction likely to change over time**

The image is set to open in a bash shell, so to start it you can use:

`docker run -it pen-test`

## Included Tools

### TCP Server and Client

Getting to grips with the basics of networks and sockets.

#### 1. TCPserver

Opens a simple TCP server on port 444 of the host. On receiving a connection, prints the incoming
address and returns a welcome message. May need to use `sudo` on local computer for port permissions.

#### 2. TCPclient

Opens a TCP client and connects to port 444 of the host. Receives any message and closes again.

#### Example - Running Docker-ised

1. Build (or pull) the image
1. Run with `docker run -it pen-test` (or whatever name you used)
1. This opens to a bash shell on the container
1. Start the server with `python3 TCPserver.py`
1. Open a second terminal and use `docker ps` to identify the running container id/name
1. In the second terminal use `docker exec [container_id/name] python3 TCPclient.py`

Since both processes are in the same container they will share a host (no need to worry about networks).
You should see connection messages in both the server and client windows.

#### Example - Docker-ised Server

1. Build (or pull) the image
1. Run with `docker run -it -p 444:444 pen-test`
1. This opens to a bash shell on the container
1. Start the server with `python3 TCPserver.py`
1. Open a second terminal and navigate to the `src` folder on your computer
1. In the second terminal use `python3 TCPclient.py`

We have mapped port 444 between the Docker container and the local computer, so connection messages will show up.

### Scanner

#### Running locally

If you are going to run the port-scanner locally, you will need to:
1. install python modules with `pip3 install -r requirements.txt`
1. install `nmap` using `apt install nmap` (or whatever package manager you use)

---

## Notes

* Using a Python image built on Alpine Linux (`python:3.7-alpine`) to minimise the
  image size
* Written on a Raspberry Pi 4 running Raspbian (Buster, 32bit), but system-agnostic. (Have had
  issues following other tutorials where images assume an AMD64 system!)


---

## Something Else Entirely 

Links that I may want at some point ...

  https://github-readme-stats.vercel.app/api?username=domwakeling&count_private=true&theme=slateorange&show_icons=true

  https://github-readme-stats.vercel.app/api/top-langs/?username=domwakeling&count_private=true&langs_count=8&hide=makefile,c,c%2B%2B,scss&layout=compact&theme=slateorange