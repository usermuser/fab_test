FROM python:3.7-alpine

WORKDIR /project

COPY ./poll_project .

RUN pip install -r requirements.txt

CMD [ "ls" ]