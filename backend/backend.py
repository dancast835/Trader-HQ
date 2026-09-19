from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins =["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Trader HQ"}

@app.get("/greetings")
def greetings():
    return {"message": "Hello React"}





if __name__ == "__backend__":
    uvicorn.run("backend:app", reload=True)
