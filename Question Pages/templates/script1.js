document.addEventListener('DOMContentLoaded', function() {
    const inputField = document.getElementById('inputField');
    const warning = document.getElementById('warning');

    inputField.addEventListener('input', function() {
        if (inputField.value.length > 1) {
            inputField.value = inputField.value.substring(0, 1000);
            warning.style.display = 'inline'; 
        } else {
            warning.style.display = 'none'; 
        }
    });
});