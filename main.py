import models
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    """
    Displays the stock screener homepage
    """
    return templates.TemplateResponse("home.html", {
        'request': request
    })

@app.post("/stock")
def create_stock():
    """
    Created a stock and store it in the database
    """
    return {
        "code":    "success",
        "message": "stock created successfully",
    }
