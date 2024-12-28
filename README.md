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

### Docker
docker-compose -f docker-compose.dev.yml up -d --build
docker-compose -f docker-compose.dev.yml down
docker-compose -f docker-compose.dev.yml down --volumes --remove-orphans
docker-compose -f docker-compose.dev.yml down --volumes --remove-orphans --rmi all
docker-compose -f docker-compose.dev.yml down --volumes --remove-orphans --rmi all --force-rm
docker-compose -f docker-compose.dev.yml down --volumes --remove-orphans --rmi all --force-rm --timeout 0
docker-compose -f docker-compose.dev.yml down --volumes --remove-orphans --rmi all --force-rm --timeout 0 --remove-orphans

cd endor_python
docker-compose -f infrastructure/docker/development/docker-compose.dev.yml up -d --build

docker-compose -f docker-compose.dev.yml down --volumes --remove-orphans
docker-compose -f docker-compose.dev.yml up -d --build