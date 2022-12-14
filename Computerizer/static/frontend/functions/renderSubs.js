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
        <form action="">
            <div class="name">
                <div>
                    <label for="f-name">First Name: <span id="error"></span></label>
                    <input class="input" type="text" name="f-name" id="f-name" placeholder="Enter your first Name"
                        required>
                </div>
                <div>
                    <label for="l-name">Last Name: <span id="error"></span></label>
                    <input class="input" type="text" name="l-name" id="l-name" placeholder="Enter your last Name"
                    required>
                </div>
            </div>
            <div>
                <label for="e-mail">Email: <span id="error"></span></label>
                <input class="input" type="email" name="e-mail" id="e-mail" placeholder="Enter your email adress"
                required>
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
    submit.addEventListener("click", subscribe)
}

function closeSignUp() {
    document.body.removeChild(logInBody)
    document.body.classList.remove("stop-scroll")
}

function subscribe(e) {
    e.preventDefault()

    const container = document.querySelector('.sign-up')
    const fName = container.querySelector('#f-name')
    const lName = container.querySelector('#l-name')
    const eMail = container.querySelector('#e-mail')

    fName.classList.remove("errorField")
    fName.previousElementSibling.firstElementChild.innerText = ''
    lName.classList.remove("errorField")
    lName.previousElementSibling.firstElementChild.innerText = ''
    eMail.classList.remove("errorField")
    eMail.previousElementSibling.firstElementChild.innerText = ''

    const backData = {
        'firstName': fName.value,
        'lastName': lName.value,
        'email': eMail.value
    }

    for (const key in backData) {
        if (backData[key] === '') {
            if (key === 'firstName') {
                fName.classList.add("errorField")
                fName.previousElementSibling.firstElementChild.innerText = "This field can't be empty!"
                return
            } else if (key === 'lastName') {
                lName.classList.add("errorField")
                lName.previousElementSibling.firstElementChild.innerText = "This field can't be empty!"
                return
            } else if (key === 'email') {
                eMail.classList.add("errorField")
                eMail.previousElementSibling.firstElementChild.innerText = "This field can't be empty!"
                return
            }
        }
    }
    
    PostSubs(backData)
    .then(res => {
        handleErrors(res)
    })
}

// handle Subscribe Errors
function handleErrors(res) {

    const container = document.querySelector('.sign-up')
    const fName = container.querySelector('#f-name')
    const lName = container.querySelector('#l-name')
    const eMail = container.querySelector('#e-mail')

    fName.classList.remove("errorField")
    lName.classList.remove("errorField")
    eMail.classList.remove("errorField")

    if (res === 'success') {
        renderThanks()
        setTimeout(closeSignUp, 2500)
    } else {
        let msg = JSON.parse(res)
        if (msg.title === "Member Exists") {
            eMail.classList.add("errorField")
            eMail.previousElementSibling.firstElementChild.innerText = "This email already exists!"
        } else {
            eMail.classList.add("errorField")
            eMail.previousElementSibling.firstElementChild.innerText = msg.detail
        }
    }
}

// Thanks msg
function renderThanks() {
    const container = document.querySelector('.sign-up')
    container.innerHTML = "<h3 class='sign__title'>Thank you for subscribing!</h3>"
}

button.addEventListener("click", renderSignSection)
buttonMobile.addEventListener("click", renderSignSection)