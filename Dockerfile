FROM python:3.9.7-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080

CMD [ "python3", "-m" , "flask", "initdb"]
CMD [ "python3","/app/app.py"]
