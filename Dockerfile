FROM ubuntu:16.04

RUN apt-get update -qq && apt-get install -yqq python python-pip

RUN pip install flask

COPY app.py /opt/

CMD [ "FLASK_APP=/opt/app.py", "flask run --host=0.0.0.0" ]
