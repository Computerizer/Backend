const postText = document.querySelector(".post__text")
let post;


const div = async () => {
    let response = await fetch('http://127.0.0.1:8000/blog/post/How to choose a CPU')
    post = await response.json()

    postText.innerHTML = post.body
}

div()