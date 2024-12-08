const form = document.getElementById("user_form")

// add a event lintener so the page should not be reload
form.addEventListener('submit', async (e) => {
    console.log("click");
    e.preventDefault() // prevent the page relaoding

    // get the form data
    const input_file = document.getElementById("audio-input");

    console.log(input_file.files[0]);

    const data = input_file.files[0]

    if (!data) {
        alert("Please Upload File")
        return
    }
    // call the api and pass the data
    await get_response(data)

})




async function get_response(data) {
    console.log("Calling API", data);
    // Create a FormData object to handle file uploads
    const formData = new FormData();
    formData.append('file', data);

    console.log(formData);
    try {
        const response = await fetch('http://127.0.0.1:8000/upload/', {
            method: "POST",
            body: formData
        })

        if (!response) {
            throw new Error("Failed to upload file. Please try again.");
        }

        // get the data
        const data = await response.json()
        console.log(data['Text']);

        const text_div = document.getElementById('audio-text')
        text_div.innerHTML = `<p>${data['Text']}</p>`


    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Check the console for details.");
    }

}
