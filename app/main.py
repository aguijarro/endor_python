from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def pong():
    return {"status": "healthy!"}