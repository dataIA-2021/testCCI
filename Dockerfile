FROM python:3.8-slim-buster

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"] # , "--port", "3000"

# UVICORN_PORT=3010 uvicorn main:app --host 0.0.0.0

# docker build -t testcci .
# docker run -d -p 3000:3000 --name goudot --restart always -e UVICORN_PORT=3000 testcci
