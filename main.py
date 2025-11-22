from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Статика
app.mount("/static", StaticFiles(directory="static"), name="static")

# Шаблоны
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = [
        # ВАЖНО: здесь ПЕРЕПУТАННЫЕ названия мы ЧИНИМ —
        # просто меняем местами title у первых двух вещей

        # 1. ТЕПЕРЬ ЭТО Jordan 4 (для картинки pants.jpg)
        {
            "title": "Jordan 4 University Blue",
            "price": "14 000 ₽",
            "image": "pants.jpg",
        },
        {
            "title": "Пуховик Moncler",
            "price": "22 000 ₽",
            "image": "jacket.jpg",
        },
        # 3. А ЭТО ТЕПЕРЬ Кастомные джинсы (для картинки jordan.jpg)
        {
            "title": "Кастомные джинсы",
            "price": "7 000 ₽",
            "image": "jordan.jpg",
        },
        {
            "title": "NIN Oversize Sweatshirt",
            "price": "8 500 ₽",
            "image": "sweatshirt.jpg",
        },

        # НОВЫЕ ВЕЩИ
        {
            "title": "White Cross Longsleeve",
            "price": "6 000 ₽",
            "image": "cross_longsleeve.jpg",
        },
        {
            "title": "Sprayground Shark Backpack",
            "price": "9 000 ₽",
            "image": "shark_backpack.jpg",
        },
        {
            "title": "Ушанка зимняя",
            "price": "4 000 ₽",
            "image": "ushanka.jpg",
        },
        {
            "title": "Brushed Black Jeans",
            "price": "6 500 ₽",
            "image": "brush_jeans.jpg",
        },
        {
            "title": "Comme des Garçons PLAY Tee",
            "price": "5 500 ₽",
            "image": "cdg_tee.jpg",
        },
        {
            "title": "Margiela Red Custom",
            "price": "12 000 ₽",
            "image": "margiela_red.jpg",
        },
        {
            "title": "Rick Owens Boots",
            "price": "18 000 ₽",
            "image": "rick_boots.jpg",
        },
        {
            "title": "Chrome Hearts Longsleeve",
            "price": "7 500 ₽",
            "image": "ch_longsleeve.jpg",
        },
    ]

    return templates.TemplateResponse(
        "items.html",
        {"request": request, "vacancies": data},
    )
