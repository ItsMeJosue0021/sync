alternateImageDisplay()

function alternateImageDisplay() {
    const images = document.querySelectorAll('.images img');
    let currentIndex = 0;

    function hideAllImages() {
        images.forEach(img => {
            img.classList.add('hidden');
        });
    }

    function showNextImage() {
        hideAllImages();
        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].classList.remove('hidden');
    }

    images[currentIndex].classList.remove('hidden');
    setInterval(showNextImage, 4000);
}