// static/js/script.js

document.addEventListener('DOMContentLoaded', () => {
    console.log("Casta.shop: JS loaded");

    const detailButtons = document.querySelectorAll('.details-btn');
    const preorderButtons = document.querySelectorAll('.preorder-btn');

    const itemModal = document.getElementById('item-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalDesc = document.getElementById('modal-desc');
    const modalPrice = document.getElementById('modal-price');
    const modalClose = document.getElementById('modal-close');

    const categoryButtons = document.querySelectorAll('.category-btn');
    const cards = document.querySelectorAll('.item-card');

    // Описания вещей для "Подробнее"
    const descriptions = {
        "Кастомные джинсы": "Ручной кастом, каждая пара уникальна. Плотный деним, аккуратный клеш и эффект краски — словно только из арт-студии.",
        "Пуховик Moncler": "Фирменный пуховик для холодной зимы: лёгкий, очень тёплый и с узнаваемым силуэтом. Идеален под городскую зиму.",
        "Jordan 4 University Blue": "Культовые Jordan 4 в цвете University Blue. Замша, комфорт и баскетбольный олдскул в одном кроссе.",
        "NIN Oversize Sweatshirt": "Оверсайз свитшот с атмосферным принтом Nine Inch Nails. Винтажный эффект и плотный хлопок.",
        "White Cross Longsleeve": "Лонгслив с крестом и лёгким винтажным эффектом. Смотрится как архивная вещь из гардероба скейтера.",
        "Sprayground Shark Backpack": "Рюкзак Sprayground с фирменной 'акульей' пастью и клетчатым паттерном. Вместительный и заметный.",
        "Ушанка зимняя": "Тёплая ушанка с мягким мехом. Носится с паркой, пуховиком и любым зимним луком.",
        "Brushed Black Jeans": "Чёрные джинсы с эффектом 'выжатой' ткани и лёгким клёшем. Хорошо сидят по фигуре.",
        "Comme des Garçons PLAY Tee": "Классический серый tee с красным сердцем CdG Play. Чистая база под любой аутфит.",
        "Margiela Red Custom": "Кастомные кроссы в стиле Margiela: красно-белый арт на верхе, винтажная подошва.",
        "Rick Owens Boots": "Высокие ботинки в духе Rick Owens — массивная подошва, контрастные панели и панк-настроение.",
        "Chrome Hearts Longsleeve": "Чёрный лонгслив с белыми принтами в стиле Chrome Hearts. Идеален под тёмный гардероб."
    };

    function openModal() {
        itemModal.classList.add('modal--visible');
        document.body.classList.add('no-scroll');
    }

    function closeModal() {
        itemModal.classList.remove('modal--visible');
        document.body.classList.remove('no-scroll');
    }

    // Режим "Подробнее"
    function openDetailsModal(title, price) {
        modalTitle.textContent = title;
        modalDesc.textContent = descriptions[title] || "Уникальная вещь из сегодняшней подборки Casta.shop.";
        modalPrice.textContent = price;
        openModal();
    }

    // Режим "Предзаказ"
    function openPreorderModal(title, price) {
        modalTitle.textContent = `Предзаказ: ${title}`;
        modalPrice.textContent = price;

        modalDesc.textContent =
            `Вы хотите оформить предзаказ на «${title}». ` +
            `Мы проверим наличие вещи, уточним размер, город и удобный способ передачи, ` +
            `после чего закрепим бронирование за вами. ` +
            `Здесь будет название тгк с обработкой заказа`;

        openModal();
    }

    // Слушатели кнопок "Подробнее"
    detailButtons.forEach(button => {
        button.addEventListener('click', () => {
            const title = button.dataset.itemTitle;
            const price = button.dataset.itemPrice;
            openDetailsModal(title, price);
        });
    });

    // Слушатели кнопок "Предзаказ"
    preorderButtons.forEach(button => {
        button.addEventListener('click', () => {
            const title = button.dataset.itemTitle;
            const price = button.dataset.itemPrice;
            openPreorderModal(title, price);
        });
    });

    // Закрытие модалки
    modalClose.addEventListener('click', closeModal);

    itemModal.addEventListener('click', (e) => {
        if (e.target === itemModal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal();
        }
    });

    // ===== Фильтр по категориям =====
    categoryButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const selected = btn.dataset.category;

            // активная кнопка
            categoryButtons.forEach(b => b.classList.remove('category-btn--active'));
            btn.classList.add('category-btn--active');

            // фильтрация карточек
            cards.forEach(card => {
                const cardCat = card.dataset.category;
                if (selected === 'all' || cardCat === selected) {
                    card.style.display = "";
                } else {
                    card.style.display = "none";
                }
            });
        });
    });
});
