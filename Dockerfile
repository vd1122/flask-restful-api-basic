# python
FROM python:3.8.1-slim-buster

# flask app directory
WORKDIR /usr/src/team-app

# project dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/team-app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/team-app/

# app port
EXPOSE 5000

# flask app
CMD ["python", "app.py"]
