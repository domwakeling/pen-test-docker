# start with a lite version of python3
FROM python:3.7-alpine
# set the working directory (use early, not going to change)
WORKDIR /app
# install nmap (use early, not going to change)
RUN apk --no-cache add nmap nmap-scripts
# copy requirements.txt & install; ahead of sopying source code, unlikely to change much
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
# copy the src folder to /app; penultimate since this *will* change most frequently
COPY ./src /app
# open a shell
CMD ["/bin/sh"]
