const button = document.querySelector(".sign-up_btn")
const buttonMobile = document.querySelector(".sign-up_mobile")
const logInBody = document.createElement("div")
let logedIn = ""


function renderSignSection(e) {
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
            <div>
                <label for="e-mail">Password:</label>
                <input class="input" type="password" name="" id="" placeholder="Enter a password">
            </div>
            <button type="submit" class="form-submit">Sign up</button>
        </form>
        <p>Do you have an account? <button class="sign-in-toggle">Sign in</button></p>
    </div>
    `
    document.body.classList.add("stop-scroll")
    document.body.appendChild(logInBody)
    let close = document.querySelector(".close__sign-up")
    let submit = document.querySelector(".form-submit")
    close.addEventListener("click", closeSignUp)
    submit.addEventListener("click", closeSignUp)
    logedIn = document.querySelector(".sign-in-toggle")
    logedIn.addEventListener("click", logedInRender)
}

function closeSignUp() {
    document.body.removeChild(logInBody)
    document.body.classList.remove("stop-scroll")
}

function logedInRender() {
    logInBody.innerHTML = `
    <div class="sign-up">
        <button class="close__sign-up">
            <i class="material-icons ">
                cancel
            </i>
        </button>
        <h3 class="sign__title">
            Sign in with your account
        </h3>
        <form action="" class="sign_form">
            <div>
                <label for="e-mail">Email:</label>
                <input class="input" type="email" name="e-mail" id="" placeholder="Enter your account email">
            </div>
            <div>
                <label for="e-mail">Password:</label>
                <input class="input" type="password" name="" id="" placeholder="Enter your account password">
            </div>
            <button type="submit" class="form-submit">Sign in</button>
        </form>
        <p>You don't have an account? <button class="sign-up-toggle">Sign up</button></p>
    </div>
    `
    logedIn = document.querySelector(".sign-up-toggle")
    logedIn.addEventListener("click", signUpRender)
    let close = document.querySelector(".close__sign-up")
    let submit = document.querySelector(".form-submit")
    close.addEventListener("click", closeSignUp)
    submit.addEventListener("click", closeSignUp)
}

function signUpRender() {
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
                    <input class="input" type="text" name="f-name" id="" placeholder="First Name">
                </div>
                <div>
                    <label for="l-name">Last Name:</label>
                    <input class="input" type="text" name="l-name" id="" placeholder="Last Name">
                </div>
            </div>
            <input class="input" type="email" name="" id="" placeholder="E-mail">
            <input class="input" type="password" name="" id="" placeholder="Password">
            <button type="submit" class="form-submit">Sign up</button>
        </form>
        <p>Do you have an account? <button class="sign-in-toggle">Sign in</button></p>
    </div>
    `
    logedIn = document.querySelector(".sign-in-toggle")
    logedIn.addEventListener("click", logedInRender)
    let close = document.querySelector(".close__sign-up")
    let submit = document.querySelector(".form-submit")
    close.addEventListener("click", closeSignUp)
    submit.addEventListener("click", closeSignUp)
}

button.addEventListener("click", renderSignSection)
buttonMobile.addEventListener("click", renderSignSection)