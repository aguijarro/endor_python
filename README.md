### FastAPI Project

This is a FastAPI project template. 

### Requirements

- Python 3.10+
- FastAPI 0.109.2
- Uvicorn 0.27.1


### Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r base.txt
```

### Installation

1. Clone the repository
2. Install the dependencies
3. Run the development server

```bash
pip install -r requirements/base.txt
uvicorn app.main:app --reload
uvicorn app.main:app --port 8001
```

### Installation

git checkout -b develop main
git checkout -b feature/MLO-1 develop
git checkout develop
git merge --no-ff feature/MLO-1
git branch -d feature/MLO-1
git push origin develop
