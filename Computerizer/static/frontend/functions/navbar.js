const menuButton = document.querySelector(".menu__btn")
const menuElm = document.querySelector(".menus__mobile")
const closeBtn = document.querySelector(".close__menu")

menuButton.addEventListener("click", () => {
    menuElm.classList.remove("hide")
})

closeBtn.addEventListener("click", () => {
    menuElm.classList.add("hide")
})

