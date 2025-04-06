from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.utils.overlay import overlay_fashion_item
import shutil
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/tryon")
async def tryon(request: Request, category: str = Form(...), item: str = Form(...), file: UploadFile = File(...)):
    upload_dir = "app/static/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    image_path = os.path.join(upload_dir, file.filename)
    with open(image_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    output_path = overlay_fashion_item(image_path, category, item)
    return FileResponse(output_path, media_type="image/png")
