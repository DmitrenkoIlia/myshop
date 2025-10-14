document.addEventListener('DOMContentLoaded', () => {
    document.body.addEventListener('submit', async (event) => {
        const form = event.target.closest('form');
        const button = form ? form.querySelector('.wishlist-toggle-btn') : null;

        if (button) {
            event.preventDefault();

            try {
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: new FormData(form),
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                });

                if (!response.ok) throw new Error('Server response not ok');

                const data = await response.json();

                if (data.status === 'ok') {
                    const likedIconSrc = button.dataset.likedSrc;
                    const unlikedIconSrc = button.dataset.unlikedSrc;

                    if (data.action === 'added') {
                        button.innerHTML = `<img src="${likedIconSrc}" alt="В избранном">`;
                        button.classList.add('active');
                    } else {
                        button.innerHTML = `<img src="${unlikedIconSrc}" alt="Добавить в избранное">`;
                        button.classList.remove('active');
                    }
                    const countElement = document.getElementById('wishlist-count');
                    if (countElement) {
                        countElement.textContent = data.wishlist_count;
                    }
                }
            } catch (error) {
                console.error('Wishlist toggle failed:', error);
            }
        }
    });
});