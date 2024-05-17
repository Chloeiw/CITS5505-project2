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
        .then(response => response.json())
        .then(data => {
            if (data.message === "Login successful") {
                showAlert(data.message);
                document.getElementById('username').innerText = data.username;
                const authButton = document.getElementById('authButton');
                authButton.innerText = 'Profile';
                authButton.onclick = function() {
                    window.location.href = "/profile";
                };
                closeModal();
            } else {
                showAlert(data.message);
            }
        });
    } else {
        showAlert('Input the Correct Username and Password!');
    }
}

function navigateToProfile() {
    window.location.href = "/profile";
}
