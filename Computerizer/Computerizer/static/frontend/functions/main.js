let posts = ""
let sales = ""
let fetchPostNum = 7
const sliderDiv = document.querySelector(".slider")
const sliderMainDiv = document.querySelector(".slider__main")
const sliderNavDiv = document.querySelector(".slider__nav")
const postsDiv = document.querySelector(".posts")
const loadMoreBtn = document.querySelector(".load-more")



// Feching data
let mainFunc = async () => {
    let response = await fetch(`http://127.0.0.1:8000/blog/recent-posts/${fetchPostNum}`)
    posts = await response.json()

    slider()
    addRecentPossts()

    let response2 = await fetch('http://127.0.0.1:8000/blog/sales/4')
    sales = await response2.json()
    addSales()

}

function selectPsot(e) {
    if (e.target.nodeName === 'H3') {
        sliderMainDiv.querySelector(".post-title").textContent = e.target.innerHTML
        console.log(e.target.id)
        sliderMainDiv.style.backgroundImage = `url('${e.target.id}')`
    }
}

function loadMore(e) {
    e.preventDefault
    addRecentPossts(fetchPostNum)
    const loadMoreBtn = document.querySelector(".load-more")
    loadMoreBtn.style.display = "none"
}

function slider() {
    let fragmentDiv = document.createDocumentFragment()
    for (let i = 0; i < 4; i++) {
        let cardDiv = document.createElement("div")
        cardDiv.classList.add("post-card")
        cardDiv.innerHTML = `
            <i class="material-icons">
                format_align_justify
            </i>
            <div class="card-text">
                <h3 class="post-card__title" id="${posts[i].image}">
                    ${posts[i].title}
                </h3>
                <p>${posts[i].description}</p>
            </div>
        `
        fragmentDiv.appendChild(cardDiv)
    }
    sliderNavDiv.appendChild(fragmentDiv)

    sliderMainDiv.firstElementChild.innerHTML = `
    <h1 class="post-title">
        ${posts[0].title}
    </h1>
    <button type="submit">Read More</button>
    `
    sliderMainDiv.style.backgroundImage = `url('${posts[0].image}')`
}

sliderNavDiv.addEventListener("click", selectPsot)

function addRecentPossts(n = 3) {
    let m = n - 3
    const postsFrag = document.createDocumentFragment()
    for (let i = m; i < n; i++) {
        let postDiv = document.createElement("div")
        postDiv.classList.add("post")
        
        postDiv.innerHTML = `
        <hr>
        <div class="post__body" >
            <img src="${posts[i].image}" alt="img">
            <div class="post__info">
                <div class="post__info__body">
                    <h3 class="post__title">
                        ${posts[i].title}
                    </h3>
                    <span class="auther">
                        ${posts[i].author}
                    </span>
                    <p class="post__prev">
                        ${posts[i].description}
                    </p>
                </div>
                <div class="post__action">
                    <span class="time">${posts[i].add_date.slice(0, 10)}</span>
                    <button>Read more</button>

                </div>
            </div>
        </div>
        `
        postsFrag.appendChild(postDiv)
    }
    postsDiv.appendChild(postsFrag)
}

loadMoreBtn.addEventListener('click', loadMore)

function addSales() {
    console.log(sales[0].part)
    for (part of sales) {
        let partDiv = document.querySelector(`.${part.part}`)
        partDiv.querySelector("a").href = part.link
        partDiv.querySelector("p").innerText = part.body
        partDiv.querySelector("img").src = part.image
    }
}

// Start the program
mainFunc()



