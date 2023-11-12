FROM python:3.11

COPY . .

COPY data/.en[v] ./.env

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]