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
        # ВАЖНО: тут уже учтён наш прошлый своп названий
        # pants.jpg -> Jordan 4
        {
            "title": "Jordan 4 University Blue",
            "price": "14 000 ₽",
            "image": "pants.jpg",
            "category": "footwear",   # Обувь
        },
        {
            "title": "Пуховик Moncler",
            "price": "22 000 ₽",
            "image": "jacket.jpg",
            "category": "tops",       # Верх
        },
        # jordan.jpg -> Кастомные джинсы
        {
            "title": "Кастомные джинсы",
            "price": "7 000 ₽",
            "image": "jordan.jpg",
            "category": "bottoms",    # Низ
        },
        {
            "title": "NIN Oversize Sweatshirt",
            "price": "8 500 ₽",
            "image": "sweatshirt.jpg",
            "category": "tops",
        },

        # НОВЫЕ ВЕЩИ
        {
            "title": "White Cross Longsleeve",
            "price": "6 000 ₽",
            "image": "cross_longsleeve.jpg",
            "category": "tops",
        },
        {
            "title": "Sprayground Shark Backpack",
            "price": "9 000 ₽",
            "image": "shark_backpack.jpg",
            "category": "accessories",
        },
        {
            "title": "Ушанка зимняя",
            "price": "4 000 ₽",
            "image": "ushanka.jpg",
            "category": "accessories",
        },
        {
            "title": "Brushed Black Jeans",
            "price": "6 500 ₽",
            "image": "brush_jeans.jpg",
            "category": "bottoms",
        },
        {
            "title": "Comme des Garçons PLAY Tee",
            "price": "5 500 ₽",
            "image": "cdg_tee.jpg",
            "category": "tops",
        },
        {
            "title": "Margiela Red Custom",
            "price": "12 000 ₽",
            "image": "margiela_red.jpg",
            "category": "footwear",
        },
        {
            "title": "Rick Owens Boots",
            "price": "18 000 ₽",
            "image": "rick_boots.jpg",
            "category": "footwear",
        },
        {
            "title": "Chrome Hearts Longsleeve",
            "price": "7 500 ₽",
            "image": "ch_longsleeve.jpg",
            "category": "tops",
        },
        {
            "title": "Лёха",
            "price": "Бесценно",
            "image": "leha.jpg",
            "category": "leha",
        }

    ]

    return templates.TemplateResponse(
        "items.html",
        {"request": request, "vacancies": data},
    )
