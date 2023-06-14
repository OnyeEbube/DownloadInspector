chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  // Listen for messages from the extension popup or content script
  if (message.action === 'checkMalicious') {
    // Extract the download link from the message
    const downloadLink = message.downloadLink;

    // Send a POST request to the Flask app endpoint
    fetch('http://localhost:5000/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ downloadLink }),
    })
    .then(response => response.json()) // Parse the response as JSON
    .then(data => {
      // Extract the result from the response data
      const isMalicious = data.is_malicious;
      // Send the result back as a response to the extension or content script
      sendResponse({ isMalicious });
    })
    .catch(error => {
      // Handle any errors that occurred during the request
      console.error(error);
      sendResponse({ error: 'An error occurred while checking the link.' });
    });

    // Return true to indicate that the response will be sent asynchronously
    return true;
  }
});
