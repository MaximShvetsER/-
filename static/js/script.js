// static/js/script.js
console.log("Vacancy Portal: JavaScript loaded!");

document.addEventListener('DOMContentLoaded', function() {
    // Находим все кнопки «Подробнее»
    const detailButtons = document.querySelectorAll('.details-btn');

    // Добавляем слушатель событий к каждой кнопке
    detailButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Получаем данные о вакансии из data-атрибутов кнопки
            const vacancyId = this.dataset.vacancyId;
            const vacancyTitle = this.dataset.vacancyTitle;

            // Выводим информацию во всплывающем окне
            alert(`Вы выбрали вакансию:\n\nID: ${vacancyId}\nНазвание: "${vacancyTitle}"\n\n(В реальном приложении здесь был бы переход на страницу с полной информацией)`);

            // Также выводим в консоль для отладки
            console.log(`Clicked on details for Vacancy ID: ${vacancyId}, Title: "${vacancyTitle}"`);
        });
    });
});