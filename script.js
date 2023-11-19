document.addEventListener("DOMContentLoaded", function () {
    // Add event listeners to sidebar links
    const sidebarLinks = document.querySelectorAll('.ul li a');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', handleSidebarClick);
    });

    // Check if a user is already logged in
    checkLoggedInUser();
});
function handleSidebarClick(event) {
    event.preventDefault();
    const pageUrl = this.getAttribute('href');
    
    // Redirect to the clicked page
    window.location.href = pageUrl;

    // Load the content of the clicked page into the 'content' div
    fetch(pageUrl)
        .then(response => response.text())
        .then(html => {
            document.querySelector('.content').innerHTML = html;
        })
        .catch(error => console.error('Error loading page:', error));
}

function checkLoggedInUser() {
    // Your existing logic for checking the logged-in user
}

// Modify the redirectToMainPage function
function redirectToMainPage() {
    // Redirect to the default page (e.g., dashboard.html)
    const defaultPageUrl = 'courses.html';
    handleSidebarClick({ target: { getAttribute: () => defaultPageUrl } });
}
document.addEventListener("DOMContentLoaded", function () {
    // Retrieve user information from local storage
    const userData = JSON.parse(localStorage.getItem('loggedInUser'));

    // Display user information on the main page
    if (userData) {
        const accountPhoto = document.getElementById('account-photo');
        const accountName = document.getElementById('account-name');

        // Update the main page elements with user information
        accountName.textContent = userData.email; // You can use any user-related data here
        // For simplicity, use a placeholder image
        accountPhoto.src = "placeholder.jpg";
        accountPhoto.alt = "Account Photo";
    }
});
function checkLoggedInUser() {
    // Retrieve user information from local storage
    const userData = JSON.parse(localStorage.getItem('loggedInUser'));

    // Display user information on the main page
    if (userData) {
        const accountName = document.getElementById('loggedInUser');
        const accountEmail = document.getElementById('loggedInEmail');

        // Update the main page elements with user information
        accountName.textContent = userData.username; // Use the actual property for the username
        accountEmail.textContent = userData.email; // Use the actual property for the email
    }
}

