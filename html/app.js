// Defining the button
const button = document.getElementById('buttonlogin');

// When the user clicks on the button
button.addEventListener('click', function handleClick() {
    setTimeout(function(){
        window.location.href = "/login.html";
    }, 100);
});