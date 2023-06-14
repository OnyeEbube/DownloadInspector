document.addEventListener('DOMContentLoaded', function () {
  // Get references to the necessary elements
  const form = document.getElementById('linkForm');
  const input = document.getElementById('link');
  const loadingMessage = document.getElementById('loadingMessage');

  // Add event listener to the form submission
  form.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior
    const downloadLink = input.value; // Get the value of the input field

    showLoadingMessage(); // Show the loading message

    // Send a message to the background script to check the malicious status of the download link
    chrome.runtime.sendMessage({ action: 'checkMalicious', downloadLink }, function (response) {
      const isMalicious = response.isMalicious; // Get the malicious status from the response
      hideLoadingMessage(); // Hide the loading message

      // Display an alert based on the malicious status
      if (isMalicious) {
        alert('The download link is malicious.');
      } else {
        alert('The download link is safe.');
      }
    });
  });

  // Show the loading message
  function showLoadingMessage() {
    loadingMessage.style.display = 'block';
  }

  // Hide the loading message
  function hideLoadingMessage() {
    loadingMessage.style.display = 'none';
  }
});
