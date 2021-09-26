FROM python:3.9.7-buster
WORKDIR /app
COPY . .
RUN python3 -m pipenv install
EXPOSE 8080

CMD [ "python3", "-m" , "flask", "initdb"]
CMD ["python3","app.py"]
