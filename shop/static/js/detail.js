    function changeImage(imageUrl, clickedThumbnail) {
        document.getElementById('mainImage').src = imageUrl;

        let thumbnails = document.querySelectorAll('.thumbnail');
        thumbnails.forEach(thumb => thumb.classList.remove('active'));
        clickedThumbnail.classList.add('active');
    }

    document.addEventListener('DOMContentLoaded', function() {
        let firstThumbnail = document.querySelector('.thumbnail');
        if (firstThumbnail) {
            firstThumbnail.classList.add('active');
        }
    });