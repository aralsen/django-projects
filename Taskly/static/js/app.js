document.addEventListener('DOMContentLoaded', function() {
    const alertMessages = document.querySelectorAll('.alert-fixed');
    alertMessages.forEach(alert => {
        if (alert.classList.contains('alert-success')) {
            alert.style.display = 'block';
            setTimeout(() => {
                alert.style.display = 'none';
            }, 3000);
        }
    });
});
