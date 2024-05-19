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
                const authButton = document.getElementById('authButton');
                if (usernameElement && authButton) {
                    usernameElement.innerText = username;
                    authButton.innerText = 'Profile';
                    authButton.onclick = function() {
                        window.location.href = "/profile";
                    };
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
                const authButton = document.getElementById('authButton');
                if (usernameElement && authButton) {
                    usernameElement.innerText = data.username;
                    authButton.innerText = 'Profile';
                    authButton.onclick = function() {
                        window.location.href = "/profile";
                    };
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