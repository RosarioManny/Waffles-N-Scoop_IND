document.addEventListener("DOMContentLoaded",() => {
  // Grabs elements
  const carousel = document.querySelector("[data-carousel");
  const slides = document.querySelector("[data-slides");

  // Keep track of index
  let currentIdx = 0;
  // Track scrolling position
  let isScrollingRight = true;

  // Move carousel
  const moveCarousel = () => {
    const totalSlides = slides.children.length;

    if(isScrollingRight) {
      // Move by 1
      currentIdx++;
      // If at middle of list reverse
      if (currentIdx >= totalSlides - 3) {
        isScrollingRight = false;
      }
    } else  {
      // Move backwards
      currentIdx--;
      // If reach the first image, stop and reverse
      if (currentIdx < 0) {
        currentIdx = 0;
        isScrollingRight = true
      }
    }
    
    slides.style.transform = `translateX(-${currentIdx * 33.34}%)`;
  }
  setInterval(moveCarousel, 2700);
})