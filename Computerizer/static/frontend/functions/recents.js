let posts = ""
let sales = ""
let readMoreBtn = ""
let fetchPostNum = 1000
let postFetched = 0
const sliderDiv = document.querySelector(".slider")
const sliderMainDiv = document.querySelector(".slider__main")
const sliderNavDiv = document.querySelector(".slider__nav")
const postsDiv = document.querySelector(".posts")
const loadMoreBtn = document.querySelector(".load-more")



// Feching data & main function
let mainFunc = async () => {
<<<<<<< HEAD
    let response = await fetch(`http://computerizr/blog/recent-posts/${fetchPostNum}`)
=======
    let response = await fetch(`http://127.0.0.1:8000/blog/recent-posts/${fetchPostNum}`)
>>>>>>> New-Frontend
    posts = await response.json()
    fetchPostNum = posts.length

    addRecentPossts()
    readMoreBtn.forEach(btn => {
        btn.addEventListener("click", redirectUrl)
    });
    loadMoreBtn.addEventListener('click', loadMore)
    
}


//  Rendering posts

function addRecentPossts() {
    postFetched+= 4
    if ((fetchPostNum - postFetched) >= 0) {
        const postsFrag = document.createDocumentFragment()
        for (let i = (postFetched - 4); i < postFetched; i++) {
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
<<<<<<< HEAD
                        <span class="time">${posts[i].add_date.slice(0, 10)}</span>
=======
                        <span class="time">${posts[i].publish_date.slice(0, 10)}</span>
>>>>>>> New-Frontend
                        <button class="read_more" value="${posts[i].title}">Read more</button>
                    </div>
                </div>
            </div>
            `
            postsFrag.appendChild(postDiv)
        }
        postsDiv.appendChild(postsFrag)
    } else {
        const loadMoreBtn = document.querySelector(".load-more")
        loadMoreBtn.style.display = "none"
    }
    readMoreBtn = document.querySelectorAll(".read_more")
}

// Lsiteners functions 
function loadMore(e) {
    e.preventDefault
    addRecentPossts()
    readMoreBtn.forEach(btn => {
        btn.addEventListener("click", redirectUrl)
    });
}

function redirectUrl(e) {
    e.preventDefault()
    window.location.href = window.location.href.slice(-8, 0) + `/post/${e.target.value}`
}

// Start file

mainFunc()