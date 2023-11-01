// gallery-navigation.js

let imageUrls = []; // Array to store image URLs
let currentIndex = 0; // Index of the currently displayed image
let newWindow = null; // Reference to the new window

// Function to open the image window
function openImageWindow(imageUrl, images) {
  imageUrls = images;
  currentIndex = imageUrls.indexOf(imageUrl);
  const width = 800; // Set the desired width of the new window
  const height = 600; // Set the desired height of the new window

  // Calculate the left and top positions for centering the new window
  const left = (window.innerWidth - width) / 2;
  const top = (window.innerHeight - height) / 2;

  // Open a new window with the specified dimensions and URL
  newWindow = window.open(imageUrl, '', `width=${width},height=${height},left=${left},top=${top}`);

  // Focus the new window (optional)
  if (newWindow) {
    newWindow.focus();
  }

  // Set up a listener to handle keyboard events for the new window
  newWindow.addEventListener("keydown", function(event) {
    if (event.key === "ArrowLeft") {
      // Previous image (left arrow key)
      currentIndex = (currentIndex - 1 + imageUrls.length) % imageUrls.length;
      const imageUrl = imageUrls[currentIndex];
      newWindow.location.href = imageUrl;
    } else if (event.key === "ArrowRight") {
      // Next image (right arrow key)
      currentIndex = (currentIndex + 1) % imageUrls.length;
      const imageUrl = imageUrls[currentIndex];
      newWindow.location.href = imageUrl;
    }
  });
}
