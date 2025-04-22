document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM fully loaded and parsed. Listening for form submission...");

    const form = document.getElementById('contact-form');
    if (!form) {
        console.error("Form with id 'contact-form' not found!");
        return;
    }

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        console.log("Form submitted. Preparing to send data to backend...");

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const subject = document.getElementById('subject').value;
        const message = document.getElementById('message').value;

        console.log("Form Data:", { name, email, subject, message });

        if (!name || !email || !subject || !message) {
            console.error("Validation failed: All fields are required.");
            alert("All fields are required.");
            return;
        }

        try {
            console.log("Sending data to backend...");
            const response = await fetch('http://127.0.0.1:5000/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, subject, message }),
            });

            const data = await response.json();
            console.log("Response received from backend:", data);

            if (response.ok) {
                alert(data.success || "Message sent successfully!");
            } else {
                console.error("Backend error:", data.error || "Unknown error occurred.");
                alert(data.error || "Something went wrong. Please try again.");
            }
        } catch (error) {
            console.error("Error during fetch:", error);
            alert("An error occurred. Please try again later.");
        }
    });
});
