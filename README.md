# Mailer

![Screenshot (220)](https://user-images.githubusercontent.com/48953676/118377550-34e14100-b5ce-11eb-9a02-704f9488d8bd.png)

Grapesjs newsletter builder with REST API using `fastapi` and `dataset`, for storing and posting newsletter templates to email lists, setup for easy deployment on `heroku`.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Usage

Clone the repo

```sh
$ git clone https://github.com/Ju99ernaut/mailer.git
$ cd mailer
```

Create virtual enviroment

```sh
$ python -m venv venv
```

Activate virtual enviroment

Linux/MacOS: `source venv/bin/activate`
Windows: `.\venv\Scripts\Activate.ps1` or `.\venv\Scripts\activate`

Install dependencies

```sh
$ pip install -r requirements.txt`
```

Run

```sh
$ python api/main.py --mail_username user@gmail.com --mail_password password
```

More config vars in `api/config.py` and enviroment vars in `app.json`.

Update [`grapesjs`](https://github.com/artf/grapesjs) init and plugins in [`editor.html`](api/templates/editor.html), for example switching out the [`grapesjs-preset-newsletter`](https://github.com/artf/grapesjs-preset-newsletter) with [`grapesjs-mjml`](https://github.com/artf/grapesjs-mjml).


The API should now be available at `http://127.0.0.1:8000`, editor at `http://127.0.0.1:8000/editor` and the API documentation will be available at `/docs` or `/redoc`.

Depending on the type of database backend, you may also need to install a database specific driver package. For MySQL, this is MySQLdb, for Postgres its psycopg2. SQLite support is integrated into Python.

On heroku you may come across the `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres`, you can avoid it by replacing `postgres://...` with `postgresql://...` in your connection url, or you can handle for it programmatically using something like:

```py
url = url.replace("postgres:", "postgresql:")
```


## Development

Clone the repo

```sh
$ git clone https://github.com/Ju99ernaut/app-listing-server.git
$ cd app-listing-server
```

Create virtual enviroment

```sh
$ python -m venv venv
```

Activate virtual enviroment

Linux/MacOS: `source venv/bin/activate`
Windows: `.\venv\Scripts\Activate.ps1` or `.\venv\Scripts\activate`

Install dependencies

> Use `requirements.txt` in production

```sh
$ pip install -r requirements.dev.txt`
```

Run tests

```sh
$ cd api 
$ python -m pytest
$ cd ..
```

Run

```sh
$ python api/main.py -r t
```

The API should now be available for development at `http://127.0.0.1:8000` and the API documentation will be available at `/docs` or `/redoc`. During development a sqlite database will be setup by default and the schema will be setup automatically

## Production

Depending on the type of database backend, you may also need to install a database specific driver package. For `MySQL`, this is `MySQLdb`, for `Postgres` its `psycopg2`. SQLite support is integrated into Python. By default `psycopg2` will be installed, if you're using `MySQL` then replace `psycopg2` with `MySQLdb` in `requirements.txt`.

### Using the users system

By default none of the API endpoints require authentication you can apply the built-in [dependencies](api/dependencies.py) to some of the endpoints so the require authentication or admin privileges.
The first user to register gains the admin role. Some admin only endpoints can be found in [routes/admin.py](api/routes/admin.py).
More information about fastapi dependencies can be found [here](https://fastapi.tiangolo.com/tutorial/dependencies/).

### Enviroment Variables

| `Variable` | `Description` | `Required` |
|------------|---------------|------------|
| `DATABASE_URL` | Database connection URL | `true` |
| `POOL_SIZE` | Connection pool size | `false` |
| `MAX_OVERFLOW` | max_connections = pool_size + max_overflow | `false` |
| `FRONTEND_URLS | Comma separated whitelisted domains | `false` |
| `SECRET_KEY` | Application secret key(Not required but important to setup to avoid using default) | false |

### Config Variables

| `Variable` | `Description` | `Default` |
|------------|---------------|-----------|
| `database_connection` | Database connection URL(Used if `DATABASE_URL` isn't provided) | `sqlite:///data.db` |
| `reload` | Reloads server when a file changes | `False` |
| `host` | Bind socket to this host | `127.0.0.1` |
| `port` | Bind socket to this port | `8000` |
| `prefix` | Template storage prefix(must be the same as editor) | `gjs-` |

Config variables can be placed inside a `config.txt` file, check [`example-config.txt`](example-config.txt) or during startup e.g.

```sh
$ python api/main.py --host 0.0.0.0 --port 5467
```

Recomended python version in [runtime.txt](runtime.txt)

## License

MIT
