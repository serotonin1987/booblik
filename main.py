from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"message": "Who are you?"}


@app.get('/sum')
def get_sum(a: int, b: int):
    return {"result": a + b}


@app.get('/ping')
def ping():
    return {"status": "ok"}


@app.get("/api/users")
def get_users():
    return {"message": "Список пользователей"}

@app.get('/divide')
def read_root():
    return {"message": ""}