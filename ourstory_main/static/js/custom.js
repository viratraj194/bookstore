setInterval(function() {
    const firstCard = document.querySelector(".book_card:first-child");
    const cardWidth = firstCard.offsetWidth;
    const container = document.querySelector(".cards-container");

    container.style.transition = "transform 0.5s ease-in-out";
    container.style.transform = "translateX(-" + cardWidth + "px)";

    setTimeout(function() {
        container.appendChild(firstCard);
        container.style.transition = "none";
        container.style.transform = "translateX(0)";
    }, 500);

}, 5000);




    // Get all div elements with class "box"
    const boxes = document.querySelectorAll('.catbg');

    // Define an array of 3 colors
    const colors = ["#e4e49a90", "#c2cae7c5", "#d9faf5","#d8d1d174","#f9bbe4"];

    // Generate a random number between 0 and 2 to select a color from the array
    function getRandomColor() {
        const index = Math.floor(Math.random() * 3);
        return colors[index];
    }

    // Apply a random color to each box
    boxes.forEach(function(box) {
        box.style.backgroundColor = getRandomColor();
    });
