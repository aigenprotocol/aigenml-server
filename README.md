## AigenML Flask Server

## create environment variables
#### create a .env file and put these variables
```
HOST=0.0.0.0
PORT=5000
```

### Run flask server

```
python run_server.py
```

### Database commands 

````
flask --app server db init
flask --app server db migrate -m "Migrate message"
flask --app server db upgrade
````

### How to run the uWSGI server

````
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
````