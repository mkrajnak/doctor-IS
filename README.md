# doctor-IS
PIS FIT BUT Project


## Using docker-compose
1. It will start db, apply migrations, populate db and run server on  localhost:8000
`docker-compose up`

If you need to delete data from DB:
`docker-compose down -v`
To rebuild images use `docker-compose build` or `docker-compose up --build`

## Manual
1. Assure you have database up and running
e.g. `docker run --name postgres --publish 127.0.0.1:5432:5432 -d postgres`
2. `cd mysite`
3. Migrate DB
`python manage.py migrate`
4. Populate DB
`python populate.py`
5. Run server, default: localhost:8000
`python manage.py runserver`
