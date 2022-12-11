/* Global Variables */
const absURL = 'https://computerizr.com' // website domain URL 
const baseURL = '/blog/recent-posts/'
const postsDiv = document.querySelector(".posts")
const loadMoreBtn = document.querySelector(".load-more")
let fetchPerRun = 4 + '/'
let chunkFetched = 1



// Main functions
function main() {
    getPosts(fetchPerRun, chunkFetched)
    .then((posts) => {
        renderPosts(posts)
    })

    loadMoreBtn.addEventListener('click', () => {
        chunkFetched += 1
        getPosts(fetchPerRun, chunkFetched)
        .then((posts) => {
            renderPosts(posts)
        })
    })
}


/*
*
* Script Functions
* 
*/ 


// Fetchin posts from databas function
const getPosts = async (num, chunk) => {
    const response = await fetch(absURL + baseURL + num + chunk)
    try {
        const posts = response.json()
        return posts
    } catch (error) {
        console.error('Failing to fetch posts from database!')
    }
}

// Rendring posts function
function renderPosts(posts) {
    const postsFrag = document.createDocumentFragment() // fragment varialbe

    // Looping through fetched posts
    if (posts !== "Out of range") {
        posts.forEach(post => {
        let postDiv = document.createElement("div")
        postDiv.classList.add("post")
            
        postDiv.innerHTML = `
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


// Routing function for read-more buttons
function redirectUrl(e) {
    e.preventDefault()
    window.location.href = window.location.href.slice(-8, 0) + `/${e.target.dataset.url}`
}


// Run script
main()