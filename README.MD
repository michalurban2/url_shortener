[![Sphinx](https://img.shields.io/badge/documentation-yes-brightgreen.svg)](https://choosealicense.com/licenses/mit/)
![Pytest-cov](https://img.shields.io/badge/coverage-100%25-green)
[![Beerware license](https://img.shields.io/badge/license-Beerware-yellow)](https://github.com/michalurban2/url_shortener/blob/US-003_readme/LICENSE)


# URL Shortener

A Django URL shortener app is a web application that generates short, customized links that redirect to longer URLs. It uses Django and a database to store original and short URLs, and may incorporate third-party services for URL shortening. The app is useful for simplifying the sharing of links online.

## Demo

[URL Shortener Heroku](https://heroku.com/)


## Tech Stack

**Server:** Python, Django, Django Rest Framework, Docker, Postgres


## Run Locally

Clone the project

```bash
  git clone git@github.com:michalurban2/url_shortener.git
```

Go to the project directory

```bash
  cd url_shortener
```

Set environment variables

```bash
  cp ./envs/api.default.env ./envs/api.env
  cp ./envs/postgres.default.env ./envs/postgres.env
  # set variable values
```

Start docker containers

```bash
  docker compose up
```

Go to your client and type:

```bash
    http://0.0.0.0:8000/api/schema/swagger-ui/
```

## Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file

`DJ_SECRET_KEY` - Django secret key for CSRF [gist](https://gist.github.com/michalurban2/639953c54abff33d4afde1dd2aaf5b61)

`DJ_DEBUG` - Production development mode

`DJ_ALLOWED_HOSTS` - Allowed hosts for Django

`LOGGING_LVL` - Python logging package levels

`DJ_SU_NAME` - Default superuser name

`DJ_SU_EMAIL` - Default superuser email

`DJ_SU_PASSWORD` - Default superuser password



Also variables to your ./envs/postgres.env file

`POSTGRES_USER` - Postgres root user

`POSTGRES_PASSWORD` - Postgres root password

`POSTGRES_DB` - Database name 

`POSTGRES_HOST` - Database host (Need to add docker service name)

`POSTGRES_PORT` - Database ports

## Running Tests

To run tests, run the following command

```bash
  docker compose exec api pytest
```


## Coverage report

![Coverage report](https://raw.githubusercontent.com/michalurban2/url_shortener/master/screenshots/coverage.png)


## Author

- [@michalurban2](https://github.com/michalurban2)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/michalurban2?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/micha%C5%82-urban-404686232/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/michalurban2_)
