# pythonapi

## Python Virtual Environment

### create a virtual environment
python3 -m venv venv

### Activate it
source venv/bin/activate

### Install requirements.txt

```bash

pip install -r requirements.txt
```

#### Run local server:

```bash

uvicorn backend.app.main:app --reload --reload-dir backend
```


