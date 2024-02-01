FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get -y install mariadb-client
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
CMD ["/bin/bash", "/code/command.sh"]
EXPOSE 8000