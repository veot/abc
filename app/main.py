import os
import shutil
from secrets import token_hex

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from draw import draw_circles

app = FastAPI()

TMP_DIR = "tmp"
# Remove previous images
shutil.rmtree(TMP_DIR, ignore_errors=True)
os.mkdir(TMP_DIR)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/tmp", StaticFiles(directory=TMP_DIR), name="tmp")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html.j2", {"request": request})


@app.get("/draw")
async def draw(
    red: bool = False,
    green: bool = False,
    blue: bool = True,
    amount: int = 20,
    min_r: int = 5,
    max_r: int = 200,
):
    img_path = f"tmp/abstract-circles-{token_hex(8)}.png"
    # Make sure min_r <= max_r
    min_r = min(min_r, max_r)
    draw_circles(amount, min_r, max_r, (red, green, blue), path=img_path)
    return {"path": img_path}
