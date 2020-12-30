# Introduction

This repository is intended to be an implementation of the tools described in HackerSplot's '[Python
3 for Pentesting](https://www.youtube.com/watch?v=UadqiHXfvsg&list=PLBf0hzazHTGM_dncTqO9l-0zUQYP0nNPU)'
course. Parts of his previous Python 2 course are (or were?) part of the FreecodeCamp syllabus.
However to add a wrinkle, and help learn/reinforce another new skill at the same time, I am also going
to try to 'Docker-ise' everything.

## Included Tools / Scripts

### 1. server

Opens a simple TCP server on port 444; on receiving a connection it prints the incoming address and
returns a welcome message.

---

## Notes

* Using a Python image built on Alpine Linux (`python:3.7-alpine` specifically) to minimise the
  image size
* Presently being written on a Raspberry Pi 4 running Raspbian (Buster, 32bit); trying to ensure that
  the Docker container can be run on any system though (have had some issues following other tutorials
  where the images are expecting to be running on an AMD64 system, which is frustrating)