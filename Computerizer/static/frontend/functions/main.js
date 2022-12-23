import {PostSubs}  from './handleSubs.js'

/* Global Variables */
const absURL = 'https://computerizr.com' // website domain URL 
const baseURL = '/blog/recent-posts/'
const salesURL = '/blog/sales/5'

const sliderDiv = document.querySelector(".slider")
const sliderMainDiv = document.querySelector(".slider__main")
const sliderNavDiv = document.querySelector(".slider__nav")
const postsDiv = document.querySelector(".posts")
const loadMoreBtn = document.querySelector(".load-more")
const subsBtn = document.querySelector(".subs-submit")
const subsDiv = document.querySelector(".subscribe_form")
const fName = document.getElementById('f-name')
const lName = document.getElementById('l-name')
const eMail = document.getElementById('e-mail')

let fetchPerRun = 4 + '/'
let chunkFetched = 1


// Main functions
function main() {
    getPosts(fetchPerRun, chunkFetched)
    .then((posts) => {
        renderSlider(posts)
        renderRecentPosts(posts)
    })

    getSales()
    .then((sales) => {
    renderSales(sales)
    })



    loadMoreBtn.addEventListener('click', () => {
        chunkFetched += 1
        getPosts(fetchPerRun, chunkFetched)
        .then((posts) => {
            renderRecentPosts(posts)
        })
    })

    subsBtn.addEventListener('click', subscribe)
}

/*
*
* Script Functions
* 
*/ 


// Fetching posts from databas function
const getPosts = async (num, chunk) => {
    const response = await fetch(absURL + baseURL + num + chunk)
    try {
        const posts = response.json()
        return posts
    } catch (error) {
        console.error('Failing to fetch posts from database!')
    }
}


// Fetching posts from databas function
const getSales = async () => {
    const response = await fetch(absURL + salesURL)
    try {
        const sales = response.json()
        return sales
    } catch (error) {
        console.error('Failing to fetch posts from database!')
    }
}

// Rendering Home page slider function

function renderSlider(posts) {

    // slider main post
    sliderMainDiv.firstElementChild.innerHTML = `
    <div class="text">
        <h1 class="post-title">
            ${posts[0].title}
        </h1>
        <p class="header__text">
            ${posts[0].description}
        </p>
    </div>
    <button type="submit" data-url="${posts[0].post_url}" class="read_more">
        Read More
    </button>
    `
    sliderMainDiv.style.backgroundImage = `url('${posts[0].image}')`
    sliderMainDiv.querySelector('button').addEventListener('click', redirectUrl)

    // slider nav posts
    let fragmentDiv = document.createDocumentFragment()
    let i = 0

    posts.forEach(post => {
        i +=1
        let cardDiv = document.createElement("div")
        cardDiv.classList.add("post-card")
        cardDiv.dataset.title = post.title
        cardDiv.dataset.des = post.description
        cardDiv.dataset.img = post.image
        cardDiv.dataset.url = post.post_url
        cardDiv.innerHTML = `
            <div class="card-text">
                <div class="head">
                    <i class="material-icons">
                        format_align_justify
                    </i>
                    <h3 class="post-card__title">
                        ${post.title}
                    </h3>
                </div>
                <p>${post.description}</p>
            </div>
        `
        fragmentDiv.appendChild(cardDiv)        
    });
    fragmentDiv.childNodes.forEach(card => {
        card.addEventListener('click', selectPsot)
    })
    sliderNavDiv.appendChild(fragmentDiv)
}

// Rendring recent posts function
function renderRecentPosts(posts) {
    const postsFrag = document.createDocumentFragment() // fragment varialbe

    // Looping through fetched posts
    if (chunkFetched <= 2) {
        posts.forEach(post => {
        let postDiv = document.createElement("div")
        postDiv.classList.add("post")
            
        postDiv.innerHTML = 
        `
        <hr>
        <div class="post__body" >
            <img src="${post.image}" alt="img">
            <div class="post__info">
                <div class="post__info__body">
                    <h3 class="post__title">
                        ${post.title}
                    </h3>
                    <span class="auther">
                        ${post.author}
                    </span>
                    <p class="post__prev">
                        ${post.description}
                    </p>
                </div>
                <div class="post__action">
                    <span class="time">
                    ${post.publish_date.slice(0, 10)}
                    </span>
                    <button class="read_more" data-url="${post.post_url}">
                        Read more
                    </button>
                </div>
            </div>
        </div>
        `
        postsFrag.appendChild(postDiv)
        });
        postsFrag.childNodes.forEach(post => {
            let btn = post.querySelector('.read_more')
            btn.addEventListener("click", redirectUrl)
        });
        postsDiv.appendChild(postsFrag)
    } else {
        loadMoreBtn.style.display = "none"
    }
    
}

// Rendering sales section
function renderSales(sales) {
    sales.forEach(sale => {
        let partDiv = document.querySelector(`.${sale.part_type}`)
        partDiv.querySelector("a").href = sale.link
        partDiv.querySelector("p").innerText = sale.body
        partDiv.querySelector("img").src = sale.image
        partDiv.previousSibling
    })
}

// Listener for selecting posts out of silder nav bar
function selectPsot(e) {
    let div = e.currentTarget
    sliderMainDiv.querySelector(".post-title").textContent = div.dataset.title
    let btn = sliderMainDiv.querySelector("button")
    btn.dataset.url = div.dataset.url
    sliderMainDiv.querySelector(".header__text").innerHTML = div.dataset.des
    sliderMainDiv.style.backgroundImage = `url('${div.dataset.img}')`
}

// Routing function
function redirectUrl(e) {
    e.preventDefault();
    window.location.href = window.location.href.slice(-8, 0) + `/${e.target.dataset.url}`
}

// Thanks message for subscribed user
function renderThanks() {
    subsDiv.innerHTML = ''
    document.querySelector('.subs__title').innerText = "Thanks for subscribing\n Stay computerized!"
}

// post subs fetch
function subscribe(e) {
    e.preventDefault()

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

    fName.classList.remove("errorField")
    lName.classList.remove("errorField")
    eMail.classList.remove("errorField")

    if (res === 'success') {
        renderThanks()
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


// Run script
main()
