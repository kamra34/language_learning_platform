// script.js

// Get the category from the URL
var category = window.location.pathname.split('/')[1]; // Updated to get the correct category

// Fetch the items from the Flask API
fetch('/api/'  + category) // Updated to use the correct endpoint
    .then(response => response.json())
    .then(items => {
        // Insert the items into the page
        var itemContainer = document.getElementById('item-container');
        items.forEach(item => {
            var itemElement = document.createElement('div');
            itemElement.textContent = item.title + ": " + item.description; // Assuming that items returned have 'title' and 'description' properties
            itemContainer.appendChild(itemElement);
        });
    })
    .catch(error => console.error('Error:', error));

// Add event listener for the "Back to Dashboard" button
var backButton = document.getElementById('back');
if (backButton) {
    backButton.addEventListener('click', function() {
        window.location.href = '/';
    });
}