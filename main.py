from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Farhan Ahmed Shaikh, Welcome to the world of CI/CD. Happy Learning!!!"}
