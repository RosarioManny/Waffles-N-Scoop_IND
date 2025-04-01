const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    console.log(entry)
    // Adds when first enters view.
    if (entry.isIntersecting) {
      entry.target.classList.add('show')
    } 
    // Removes when out of view. Good if you want animation to happen 
    else {
      entry.target.classList.remove('show')
    }
  })
})

const hiddenElementsSlideLeft = document.querySelectorAll('.hidden-slide-l');
const hiddenElementsSlideRight = document.querySelectorAll('.hidden-slide-r');
const hiddenElementsFade= document.querySelectorAll('.hidden-fade');
hiddenElementsSlideLeft.forEach((el) => observer.observe(el));
hiddenElementsSlideRight.forEach((el) => observer.observe(el));
hiddenElementsFade.forEach((el) => observer.observe(el));