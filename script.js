async function fetchQuote() {
    const quoteType = document.getElementById('quoteType').value;
    const endpoint = `https://beautiful-quotes.azurewebsites.net/api/beautiful_quotes?type=${quoteType}`;

    try {
        const response = await fetch(endpoint);
        const contentType = response.headers.get('content-type');

        if (response.ok) {
            if (contentType && contentType.includes('application/json')) {
                const data = await response.json();
                const quoteContainer = document.getElementById('quoteContainer');
                quoteContainer.innerHTML = `<p>${data.quote.replace("Here is your quote:", "")}</p>`;
                if (data.image) {
                    const image = document.createElement('img');
                    image.src = `data:image/png;base64,${data.image}`;
                    quoteContainer.appendChild(image);
                }
            } else {
                const data = await response.text();
                const quoteContainer = document.getElementById('quoteContainer');
                quoteContainer.innerHTML = `<p>${data}</p>`;
                const imageElement = quoteContainer.querySelector('img');
                if (imageElement) {
                    imageElement.remove(); // Remove the image if present
                }
            }
        } else {
            throw new Error('Failed to fetch quote.');
        }
    } catch (error) {
        console.error(error);
        alert('An error occurred while fetching the quote. Please try again later.');
    }
}