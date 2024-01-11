from fastapi import FastAPI
from fastapi import Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.database import SessionLocal, engine




# Import all the required libraries:





# app code starts here:
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependencies:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app gets executed here:

@app.get("/")
async def home_page(request: Request, db: SessionLocal = Depends(get_db)):

    return templates.TemplateResponse("home/index.html", {"request": request})

@app.get("/game")
async def game_page(request: Request, db: SessionLocal = Depends(get_db)):

    return templates.TemplateResponse("home/index.html", {"request": request})
# app posts execution code here:






