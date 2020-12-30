# start with a lite version of python3
FROM python:3.7-alpine
# set the working directory (early, not going to change)
WORKDIR /app
# install nmap (early, not going to change)
RUN apk --no-cache add nmap
# copy requirements.txt & install; will change less often than source code
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
# copy the src folder to /app
COPY ./src /app
# open a shell
CMD ["/bin/sh"]
