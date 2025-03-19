document.querySelector("form").addEventListener("submit", function(event) {
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;

    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Invalid email format!");
        event.preventDefault();
        return;
    }

    let phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(phone)) {
        alert("Phone number must be 10 digits.");
        event.preventDefault();
    }
});
