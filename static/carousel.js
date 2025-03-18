const button = document.querySelectorAll("[data-carousel-button]")

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const offset = button.dataset.carouselButton === "next" ? 1 : -1
    const slides = button
      .closest("[data-carousle]")
      .querySelector("[data-slides]")
    const activeSlide = slides.querySelector("[data-active]")
    let newIdx = [...slides.children].indexOf(activeSLide) + offset
    if (newIdx < 0) newIdx = slides.children.lenght - 1
    if (newIdx >= slides.children.length) newIdx = 0

    slides.children[newIdx].dataset.active = true
    delete activeSlide.dataset.active
  })
})