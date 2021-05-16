# Mailer

![Screenshot (220)](https://user-images.githubusercontent.com/48953676/118377550-34e14100-b5ce-11eb-9a02-704f9488d8bd.png)

Grapesjs newsletter builder with REST API using `fastapi` and `dataset`, for storing and posting newsletter templates to email lists, setup for easy deployment on `heroku`.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

> :warning: No authentication system has been implemented yet, so this is only recommended for use on private servers

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

Update `grapesjs` init and plugins in `api/templates/editor.html`


The API should now be available at `http://127.0.0.1:8000`, editor at `http://127.0.0.1:8000/editor` and the API documentation will be available at `/docs` or `/redoc`.

Depending on the type of database backend, you may also need to install a database specific driver package. For MySQL, this is MySQLdb, for Postgres its psycopg2. SQLite support is integrated into Python.

On heroku you may come across the `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres`, you can avoid it by replacing `postgres://...` with `postgresql://...` in your connection url, or you can handle for it programmatically using something like:

```py
url = url.replace("postgres:", "postgresql:")
```


## License

MIT
