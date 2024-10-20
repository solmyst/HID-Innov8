// Array to keep track of the history of page views
let pageHistory = [];

// Function to show a page and track history
function showPage(pageId) {
    // Get the current active page
    const currentPage = document.querySelector('.page.active');
    
    // If there is a current page, add it to the history
    if (currentPage && currentPage.id !== pageId) {
        pageHistory.push(currentPage.id);
    }

    // Hide all pages
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => {
        page.classList.remove('active');
    });

    // Show the new page
    const newPage = document.getElementById(pageId);
    if (newPage) {
        newPage.classList.add('active');
    } else {
        console.error(`Page with ID "${pageId}" not found.`);
    }
}

// Function to go back to the previous page
function goBack() {
    // Get the last page from the history
    const lastPage = pageHistory.pop();

    // If there's a last page in history, navigate to it
    if (lastPage) {
        showPage(lastPage);
    } else {
        console.log("No previous page in history.");
    }
}

