const postText = document.querySelector(".post__text")
const postTitle = document.querySelector(".post__title")
const author = document.querySelector(".author")
const dateSpan = document.querySelector(".date")
const heroImage = document.querySelector(".hero")
const recentsNav = document.querySelector(".recents__nav")
let posts = ""
let post;


const div = async () => {
    let response = await fetch('http://127.0.0.1:8000/blog/post/How to choose a CPU')
    post = await response.json()
    addPost()

    let response2 = await fetch(`http://127.0.0.1:8000/blog/recent-posts/4`)
    posts = await response2.json()
    addRecents()
}

function addPost() {
    console.log(post.publish_date)

    let dateHolder = post.publish_date.slice(0, 10)
    let holder = ""
    let date = "";

    date = dateHolder.slice(8, 10) + "/" + dateHolder.slice(5, 7) + "/" + dateHolder.slice(0, 4) 

    postTitle.innerText = post.title
    author.innerText = post.author
    dateSpan.innerText = date
    postText.innerHTML = post.body
    heroImage.src = post.image
}

function addRecents() {
    let fragmentDiv = document.createDocumentFragment()
    for (let i of posts) {
        let cardDiv = document.createElement("div")
        cardDiv.classList.add("post-card")
        cardDiv.innerHTML = `
            <img src="${i.image}" alt="post image" class="card__img">
            <div class="card__text">
                <h3 class="post-card__title" id="${i.image}">
                    ${i.title}
                </h3>
                <p>${i.description}</p>
            </div>
        `
        fragmentDiv.appendChild(cardDiv)
    }
    recentsNav.appendChild(fragmentDiv)
}

div()