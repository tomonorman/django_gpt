# Django Implementation of OpenAI GPT

## Installation and Starting a Dev Server

1. Get an openapi API key, copy `'.env-template` to `.env` and add your Key

2. Install and run migrations (sqlite3.db will be automatically created)

```
pip install -r requirements.txt
python manage.py migrate
```

3. Run a devserver

```
python manage.py runserver
```

## Changing the GPT model to be used

* L17 of `views.py` in the gpt folder