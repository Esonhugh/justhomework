FROM python:3.9.7-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080

CMD [ "sh", "/app/initdb.sh"]
