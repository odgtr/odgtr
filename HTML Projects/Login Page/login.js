// Defining the button
const button = document.getElementById('loginbutton');

// When the user clicks on the button
button.addEventListener('click', function handleClick() {
    let usr = document.getElementById('username').value
    let passwrd = document.getElementById('password').value
    if (usr == "admin" && passwrd == "root") {
        // Redirect the user in 0.1 seconds
        setTimeout(function(){
            window.location.href = "/success.html";
        }, 100);
    } else {
        alert('Incorrect username or password. (Try "admin | root")')
    }
});

let input1 = document.getElementById("username");
input1.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.getElementById('loginbutton').click();
    }
})

let input2 = document.getElementById("password");
input2.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById('loginbutton').click();
    }
})

