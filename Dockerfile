FROM python:3.11

COPY . .

COPY data/.env .env

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]