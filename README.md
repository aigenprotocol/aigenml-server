<div align="center">
<img src="https://aigenprotocol.com/static/media/aigen-logo-light.fad5403b0fa280336867e8ea8400db40.svg" />
<h2> AigenML Server </h2>
<h3>
AigenML flask server to deploy aigenml anywhere
</h3>
</div>

## create environment variables
#### create a .env file and put these variables
```
SQLALCHEMY_DATABASE_URI=sqlite:////Users/apple/aigen/aigen.db
PROJECTS_DIR=/Users/apple/aigen
HOST=0.0.0.0
PORT=5000
UPLOAD_FOLDER=uploads
```

### Database commands 

````
flask --app server db init
flask --app server db migrate -m "Migrate message"
flask --app server db upgrade
````

### Run flask server

```
python run_server.py
```

### How to run the uWSGI server

````
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
````

## License

<a href="LICENSE.rst"><img src="https://img.shields.io/github/license/aigenprotocol/aigenml-server"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE.rst) file for details
