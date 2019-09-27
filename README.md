# mshack19

## setup

```
pipenv install
```

## develop

```
pipenv shell
cd src/
uvicorn main:app --reload
```

## database

* always generated, no merge
* generate: `python create_and_fill_db.py`
