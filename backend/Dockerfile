# Base Image
FROM python:3.10

RUN apt-get update && apt-get install poppler-utils -y
# set working directory
WORKDIR /usr/src

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

# add app
COPY . /usr/src/app

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
