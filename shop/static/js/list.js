document.addEventListener('DOMContentLoaded', function () {
    
    // --- Логіка для відкриття/закриття сайдбару (без змін) ---
    const openBtn = document.getElementById('open-filter-btn');
    const closeBtn = document.querySelector('.sidebarr-close');
    const overlay = document.querySelector('.filter-overlay');
    
    const toggleFilterSidebar = () => {
        document.body.classList.toggle('filters-open');
    };

    if (openBtn) openBtn.addEventListener('click', toggleFilterSidebar);
    if (closeBtn) closeBtn.addEventListener('click', toggleFilterSidebar);
    if (overlay) overlay.addEventListener('click', toggleFilterSidebar);

    // --- Логіка для акордеону (без змін) ---
    const accordions = document.querySelectorAll(".accordion-toggle");
    accordions.forEach(accordion => {
        accordion.addEventListener("click", function() {
            this.classList.toggle("active");
            const filterOptions = this.nextElementSibling;
            if (filterOptions.style.maxHeight) {
                filterOptions.style.maxHeight = null;
            } else {
                filterOptions.style.maxHeight = filterOptions.scrollHeight + "px";
            } 
        });
    });

    // --- ОНОВЛЕНА ЛОГІКА ДЛЯ КНОПОК ФІЛЬТРАЦІЇ ---
    
    const applyBtn = document.getElementById('apply-filters-btn');
    const resetBtn = document.getElementById('reset-filters-btn');
    const filterSidebar = document.getElementById('filter-sidebar');

    // Обробник для кнопки "Застосувати" (ваш код, працює коректно)
    if (applyBtn) {
        applyBtn.addEventListener('click', function() {
            const selectedFilters = {};
            
            // 1. Знаходимо всі обрані чекбокси всередині сайдбару
            const checkedCheckboxes = filterSidebar.querySelectorAll('input[type="checkbox"]:checked');
            
            // 2. Групуємо їх за назвою (name)
            checkedCheckboxes.forEach(checkbox => {
                const name = checkbox.name;
                const value = checkbox.value;
                
                if (!selectedFilters[name]) {
                    selectedFilters[name] = [];
                }
                selectedFilters[name].push(value);
            });
            
            // 3. Створюємо рядок параметрів URL
            const params = new URLSearchParams();
            for (const key in selectedFilters) {
                // Об'єднуємо значення через кому, напр. "brand=nike,adidas"
                params.append(key, selectedFilters[key].join(','));
            }
            
            // 4. Перенаправляємо користувача на нову URL
            // `window.location.pathname` - це поточний шлях без старих параметрів
            window.location.href = `${window.location.pathname}?${params.toString()}`;
        });
    }

    // Обробник для кнопки "Скинути" (покращена версія)
    if (resetBtn) {
        resetBtn.addEventListener('click', function() {
            // Просто перенаправляємо на ту ж сторінку, але без GET-параметрів
            window.location.href = window.location.pathname;
        });
    }
});