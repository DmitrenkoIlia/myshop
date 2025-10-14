document.addEventListener('DOMContentLoaded', function () {
    
    // Елементи керування сайдбаром
    const openBtn = document.getElementById('open-filter-btn');
    const closeBtn = document.querySelector('.sidebarr-close'); // Використовуйте цей клас
    const overlay = document.querySelector('.filter-overlay');
    
    const toggleFilterSidebar = () => {
        document.body.classList.toggle('filters-open');
    };

    if (openBtn) openBtn.addEventListener('click', toggleFilterSidebar);
    if (closeBtn) closeBtn.addEventListener('click', toggleFilterSidebar);
    if (overlay) overlay.addEventListener('click', toggleFilterSidebar);

    // --- Логіка для акордеону (без змін) ---
    document.querySelectorAll(".accordion-toggle").forEach(accordion => {
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

    // --- ЛОГІКА КНОПОК ФІЛЬТРАЦІЇ ---
    const applyBtn = document.getElementById('apply-filters-btn');
    const resetBtn = document.getElementById('reset-filters-btn');
    const filterSidebar = document.getElementById('filter-sidebar');

    // Кнопка "Застосувати"
    if (applyBtn) {
        applyBtn.addEventListener('click', function() {
            const selectedFilters = {};
            
            // 1. Знайти всі обрані чекбокси
            const checkedCheckboxes = filterSidebar.querySelectorAll('input[type="checkbox"]:checked');
            
            // 2. Згрупувати їх за іменем (brand, country і т.д.)
            checkedCheckboxes.forEach(checkbox => {
                const name = checkbox.name;
                const value = checkbox.value;
                if (!selectedFilters[name]) {
                    selectedFilters[name] = [];
                }
                selectedFilters[name].push(value);
            });
            
            // 3. Створити об'єкт параметрів URL
            const params = new URLSearchParams();
            for (const key in selectedFilters) {
                // Об'єднати значення через кому, напр. "brand=funko,marvel"
                params.append(key, selectedFilters[key].join(','));
            }
            
            // 4. Перенаправити на поточну сторінку з новими параметрами
            // window.location.pathname - це чистий шлях без старих параметрів
            window.location.href = `${window.location.pathname}?${params.toString()}`;
        });
    }

    // Кнопка "Скинути"
    if (resetBtn) {
        resetBtn.addEventListener('click', function() {
            // Перенаправити на чистий шлях без будь-яких параметрів
            window.location.href = window.location.pathname;
        });
    }
});