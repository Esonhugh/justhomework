# justhoemwork 

## simple api server by flask app

## Usage :

```
pipenv --version || pip3 install pipenv
pipenv install  # install dependencies

flask initdb  # init database
python3 app.py # start server 

```

## Api docs

1. access the server.it will show on screen
2. comments in app.py

# Docker build

```bash
sudo docker build . -t flask:4.0
sudo docker run -d -p 8080:8080 flask:4.0 
```

# Now available on [api server on cloud](http://kali.esonhugh.me:8080/)