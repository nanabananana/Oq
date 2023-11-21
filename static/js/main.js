document.addEventListener("DOMContentLoaded", function () {
  // Retrieve user information from local storage
  const userData = JSON.parse(localStorage.getItem("loggedInUser"));

  // Display user information on the main page
  if (userData) {
    const accountPhoto = document.getElementById("account-photo");
    const accountName = document.getElementById("account-name");

    // Update the main page elements with user information
    accountName.textContent = userData.email; // You can use any user-related data here
    // For simplicity, use a placeholder image
    accountPhoto.src = "placeholder.jpg";
    accountPhoto.alt = "Account Photo";
  }
});
