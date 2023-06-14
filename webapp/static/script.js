document.addEventListener('DOMContentLoaded', function () {
    const loadingMessage = document.getElementById('loadingMessage');
    const form = document.querySelector('form');

    // Add event listener to the form submit event
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        showLoadingMessage(); // Show loading message
    });

    // Function to show the loading message
    function showLoadingMessage() {
        loadingMessage.style.display = 'block'; // Display the loading message
    }
});
