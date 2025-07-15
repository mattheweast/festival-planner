# pythonapi

This project is my take on Clash Finder. A way to find artist clashes at festivals but with a social twist, to see friends lineups and orcestrate who you want to see, with who you want to see them with.

## Python Virtual Environment

### create a virtual environment
```bash
python3 -m venv venv
```
### Activate it
```bash
source venv/bin/activate
```
### Install requirements.txt
```bash

pip install -r requirements.txt
```
#### Run local server:
```bash

uvicorn backend.app.main:app --reload --reload-dir backend
```
# React
### Start Frontend
```bash
npm run web
```

