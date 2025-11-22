from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = [
        {
            "title": "Кастомные джинсы",
            "price": "7 000 ₽",
            "image": "pants.jpg"
        },
        {
            "title": "Пуховик Moncler",
            "price": "22 000 ₽",
            "image": "jacket.jpg"
        },
        {
            "title": "Jordan 4 University Blue",
            "price": "14 000 ₽",
            "image": "jordan.jpg"
        },
        {
            "title": "NIN Oversize Sweatshirt",
            "price": "8 500 ₽",
            "image": "sweatshirt.jpg"
        }
    ]

    return templates.TemplateResponse(
        "items.html",
        {"request": request, "vacancies": data}
    )
