document.getElementById('submitBtn').addEventListener('click', function(event) {
    
    event.preventDefault();

    // Store the data to localStorage
    localStorage.setItem('username', document.getElementById('username').value);
    localStorage.setItem('gender', document.getElementById('gender').value);
    localStorage.setItem('occupation', document.getElementById('occupation').value);
    localStorage.setItem('selfIntro', document.getElementById('selfIntro').value);
    localStorage.setItem('password', document.getElementById('password').value);
    localStorage.setItem('securityQuestion', document.getElementById('securityQuestion').value);
    localStorage.setItem('securityAnswer', document.getElementById('securityAnswer').value);

    // Refresh the page
    window.location.reload();
});

// Retrieve the data
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('username').value = localStorage.getItem('username') || '';
    document.getElementById('gender').value = localStorage.getItem('gender') || 'Choose...';
    document.getElementById('occupation').value = localStorage.getItem('occupation') || 'Choose...';
    document.getElementById('selfIntro').value = localStorage.getItem('selfIntro') || '';
    document.getElementById('password').value = localStorage.getItem('password') || '';
    document.getElementById('securityQuestion').value = localStorage.getItem('securityQuestion') || 'Choose...';
    document.getElementById('securityAnswer').value = localStorage.getItem('securityAnswer') || '';
});