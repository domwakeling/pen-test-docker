FROM python:3.7-alpine
WORKDIR /app
RUN apk --no-cache add nmap
COPY ./src /app
#CMD ["python", "test.py"]
CMD ["/bin/sh"]
