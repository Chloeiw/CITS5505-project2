let start = 2; // Start after the initial posts
const limit = 3; // Number of posts to fetch each time

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("loadMore").addEventListener("click", function() {
        fetch(`/get_more_posts?start=${start}&limit=${limit}`)
            .then(response => response.json())
            .then(data => {
                console.log('Fetched data:', data); // Log the data to check the response

                if (data.length > 0) {
                    data.forEach(function(post) {
                        console.log('Appending post:', post); // Log each post before appending
                        document.querySelector(".question-container").insertAdjacentHTML('beforeend', `
                            <div class="question">
                                <h2><a href="/question/${post.id}">${post.title}</a></h2>
                                <hr>
                                <span class="usericon"><img src="../static/usericon.png" alt=""></span>
                                <span class="usernameComment">${post.user_id}</span>
                                <span class="lastreply">${post.post_time}</span>
                                <p>${post.content}</p>
                            </div>
                        `);
                    });
                    start += data.length; // Increment start by the actual number of posts fetched
                } else {
                    document.getElementById("loadMore").style.display = "none";
                }
            })
            .catch(error => {
                console.error('Error fetching posts:', error);
            });
    });
});

function toggleAuth() {
    document.getElementById('loginModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('loginModal').style.display = 'none';
}

function showAlert(message) {
    const alertModal = document.getElementById('alertModal');
    const alertMessage = document.getElementById('alertMessage');
    alertMessage.innerText = message;
    alertModal.style.display = 'block';
    setTimeout(() => {
        alertModal.style.display = 'none';
    }, 3000);
}

function login() {
    const username = document.getElementById('usernameInput').value;
    const password = document.getElementById('passwordInput').value;

    if (username && password) {
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username, password: password })
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(errorData => {
                    throw new Error(errorData.message || "HTTP error " + response.status);
                });
            }
            return response.json();
        })
        .then(data => {
            console.log('Response data:', data);  
            if (data.status === 200) {
                const usernameElement = document.getElementById('username');
                if (usernameElement) {
                    usernameElement.innerText = username;
                    document.getElementById('authButton').style.display = 'none'; // 登录成功后隐藏按钮
                    closeModal();
                }
            } else {
                showAlert(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);  
            showAlert('Wrong combinations! Try again.');
        });
    } else {
        showAlert('Input the Correct Username and Password!');
    }
}

function navigateToProfile() {
    window.location.href = "/profile";
}

function closeModal() {
    const loginModal = document.getElementById('loginModal');
    if (loginModal) {
        loginModal.style.display = 'none';
    }
}

function showAlert(message) {
    const alertModal = document.getElementById('alertModal');
    const alertMessage = document.getElementById('alertMessage');
    if (alertModal && alertMessage) {
        alertMessage.innerText = message;
        alertModal.style.display = 'block';
        setTimeout(() => {
            alertModal.style.display = 'none';
        }, 3000);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    checkLoginStatus();
});

function checkLoginStatus() {
    fetch('/check_login')
        .then(response => response.json())
        .then(data => {
            if (data.status === 200) {
                const usernameElement = document.getElementById('username');
                if (usernameElement) {
                    usernameElement.innerText = data.username;
                    document.getElementById('authButton').style.display = 'none'; // 如果已经登录，则隐藏按钮
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function logout() {
    fetch('/logout', {
        method: 'GET'
    })
    .then(response => {
        if (response.ok) {
            const usernameElement = document.getElementById('username');
            const authButton = document.getElementById('authButton');
            if (usernameElement && authButton) {
                usernameElement.innerText = '';
                authButton.innerText = 'Sign up / Login';
                authButton.style.display = 'block'; // 登出后显示按钮
                authButton.onclick = function() {
                    showModal();
                };
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function showModal() {
    const loginModal = document.getElementById('loginModal');
    if (loginModal) {
        loginModal.style.display = 'block';
    }
}

function closeModal() {
    const loginModal = document.getElementById('loginModal');
    if (loginModal) {
        loginModal.style.display = 'none';
    }
}