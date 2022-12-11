import {PostSubs}  from './handleSubs.js'

/* Global Variables */
const absURL = 'http://127.0.0.1:8000' // website domain URL 
const baseURL = '/blog/recent-posts/'
const salesURL = '/blog/sales/5'

const sliderDiv = document.querySelector(".slider")
const sliderMainDiv = document.querySelector(".slider__main")
const sliderNavDiv = document.querySelector(".slider__nav")
const postsDiv = document.querySelector(".posts")
const loadMoreBtn = document.querySelector(".load-more")
const subsBtn = document.querySelector(".subs-submit")

let fetchPerRun = 4 + '/'
let chunkFetched = 1


// Main functions
function main() {
    getPosts(fetchPerRun, chunkFetched)
    .then((posts) => {
        renderSlider(posts)
        renderRecentPosts(posts)
        sliderNavDiv.addEventListener("click", selectPsot)
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

    subsBtn.addEventListener('click', doSubs)

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
        cardDiv.innerHTML = `
            <div class="card-text" 
            data-title='${post.title}'
            data-des='${post.description}'
            data-img='${post.image}'
            data-url='${post.post_url}'
            >
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

    sliderNavDiv.appendChild(fragmentDiv)
}

// Rendring recent posts function
function renderRecentPosts(posts) {
    const postsFrag = document.createDocumentFragment() // fragment varialbe

    // Looping through fetched posts
    if (chunkFetched !== 2) {
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
    if (e.target.nodeName === 'H3') {
        let div = e.target.parentElement.parentElement
        sliderMainDiv.querySelector(".post-title").textContent = div.dataset.title
        let btn = sliderMainDiv.querySelector("button")
        btn.dataset.url = div.dataset.url
        btn.addEventListener('click', redirectUrl)
        sliderMainDiv.querySelector(".header__text").innerHTML = div.dataset.des
        sliderMainDiv.style.backgroundImage = `url('${div.dataset.img}')`
        
    }
}

// Routing function
function redirectUrl(e) {
    e.preventDefault()
    window.location.href = window.location.href.slice(-8, 0) + `/${e.target.dataset.url}`
}

// post subs fetch
function doSubs(e) {
    e.preventDefault()
    console.log(PostSubs('potos'))
}




// Run script
main()