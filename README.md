# pythonapi

## Python Virtual Environment

### 1. Clone the project
git clone https://github.com/yourusername/project.git
cd project

### 2. Go one level up and create a virtual environment
cd ..
python3 -m venv venv

### 3. Activate it
source venv/bin/activate

### 4. Return to the project
cd project

#### Install requirements.txt

```bash

pip install -r requirements.txt
```

#### Run local server:

```bash

uvicorn backend.app.main:app --reload --reload-dir backend
```


