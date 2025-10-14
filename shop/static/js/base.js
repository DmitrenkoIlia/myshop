document.addEventListener('DOMContentLoaded', function() {
    // --- Логика открытия/закрытия сайдбара ---
    const hamburger = document.querySelector('.humburger-menu'); // Убедитесь, что этот элемент существует
    const closeBtn = document.querySelector('.sidebar-close');
    const overlay = document.querySelector('.sidebar-overlay');

    const toggleSidebar = () => {
        // Добавляем/убираем класс, который контролирует и сайдбар, и оверлей
        document.body.classList.toggle('sidebar-open');
    };

    // Назначаем обработчики событий
    if (hamburger) hamburger.addEventListener('click', toggleSidebar);
    if (closeBtn) closeBtn.addEventListener('click', toggleSidebar);
    if (overlay) overlay.addEventListener('click', toggleSidebar);

    
    // --- Логика аккордеона ---
    const accordions = document.querySelectorAll(".accordion");

    accordions.forEach(acc => {
        acc.addEventListener("click", function() {
            this.classList.toggle("active");
            const filterList = this.nextElementSibling;

            // Плавное открытие/закрытие за счет изменения max-height
            if (filterList.style.maxHeight) {
                filterList.style.maxHeight = null; // Закрыть панель
            } else {
                // Открыть, установив высоту равной реальной высоте контента
                filterList.style.maxHeight = filterList.scrollHeight + "px";
            }
        });
    });
});