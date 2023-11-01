function openImageWindow(imageUrl) {
    const width = 800; // Set the desired width of the new window
    const height = 600; // Set the desired height of the new window

    // Calculate the left and top positions for centering the new window
    const left = (window.innerWidth - width) / 2;
    const top = (window.innerHeight - height) / 2;

    // Open a new window with the specified dimensions and URL
    const newWindow = window.open(imageUrl, '', `width=${width},height=${height},left=${left},top=${top}`);

    // Focus the new window (optional)
    if (newWindow) {
        newWindow.focus();
    }
}
