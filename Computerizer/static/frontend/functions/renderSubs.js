import {PostSubs}  from './handleSubs.js'

const button = document.querySelector(".sign-up_btn")
const buttonMobile = document.querySelector(".sign-up_mobile")
const logInBody = document.createElement("div")



function renderSignSection() {
    logInBody.classList.add("body")
    logInBody.classList.add("sign-form")
    logInBody.id = "sign-up"
    logInBody.innerHTML = `
    <div class="sign-up">
        <button class="close__sign-up">
            <i class="material-icons ">
                cancel
            </i>
        </button>
        <h3 class="sign__title">
            Become a member now!
        </h3>
        <form action="" class="sign_form">
            <div class="name">
                <div>
                    <label for="f-name">First Name:</label>
                    <input class="input" type="text" name="f-name" id="" placeholder="Enter your first Name">
                </div>
                <div>
                    <label for="l-name">Last Name:</label>
                    <input class="input" type="text" name="l-name" id="" placeholder="Enter your last Name">
                </div>
            </div>
            <div>
                <label for="e-mail">Email:</label>
                <input class="input" type="email" name="e-mail" id="" placeholder="Enter your email adress">
            </div>
            <button type="submit" class="form-submit">Subscribe</button>
        </form>
    </div>
    `
    document.body.classList.add("stop-scroll")
    document.body.appendChild(logInBody)
    let close = document.querySelector(".close__sign-up")
    let submit = document.querySelector(".form-submit")
    close.addEventListener("click", closeSignUp)
    submit.addEventListener("click", doSubs)
}

function closeSignUp() {
    document.body.removeChild(logInBody)
    document.body.classList.remove("stop-scroll")
}

function doSubs(e) {
    e.preventDefault()
    console.log(PostSubs('potos'))
}

button.addEventListener("click", renderSignSection)
buttonMobile.addEventListener("click", renderSignSection)