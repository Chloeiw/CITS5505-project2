let start = 3; // Start after the initial posts
const limit = 3; // Number of posts to fetch each time

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("loadMore").addEventListener("click", function() {
        fetch(`/get_posts?start=${start}&limit=${limit}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    start += limit;
                    data.forEach(function(post) {
                        document.querySelector(".question-container").insertAdjacentHTML('beforeend', `
                            <div class="question">
                                <h2><a href="/question/${post.question_id}">${post.question}</a></h2>
                                <hr>
                                <span class="usericon"><img src="../static/usericon.png" alt=""></span>
                                <span class="usernameComment">${post.username}</span>
                                <span class="lastreply">${post.timestamp}</span>
                                <p>${post.content}</p>
                            </div>
                        `);
                    });
                } else {
                    document.getElementById("loadMore").style.display = "none";
                }
            });
    });
});
