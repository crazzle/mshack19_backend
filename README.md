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

### docs

after starting the app, call `http://127.0.0.1:8000/docs`

## database

from `src`

* always generated, no merge
* generate: `python create_and_fill_db.py`

# generate data

from `src`

1. `python preprocessing/create_attractivity_matrix.py`
