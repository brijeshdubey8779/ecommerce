document.querySelectorAll('.increment-button').forEach(button => {
    button.addEventListener('click', function () {
        let input = this.closest('form').querySelector('[data-input-counter]');
        let currentQuantity = parseInt(input.value);
        let newQuantity = currentQuantity + 1; // Increment the quantity

        input.value = newQuantity;

        // Get CSRF token from the hidden input field
        const csrfToken = this.closest('form').querySelector('[name="csrf_token"]').value;
        let productId = this.closest('form').querySelector('[name="product_id"]').value;
        console.log(productId)
        // Send updated quantity to the backend using AJAX
        updateQuantityInBackend(productId, newQuantity, csrfToken);
    });
});

document.querySelectorAll('.decrement-button').forEach(button => {
    button.addEventListener('click', function () {
        let input = this.closest('form').querySelector('[data-input-counter]');
        let currentQuantity = parseInt(input.value);
        let newQuantity = currentQuantity - 1; // Decrement the quantity

        if (newQuantity < 1) return; // Prevent decrementing below 1

        input.value = newQuantity;

        // Get CSRF token from the hidden input field
        const csrfToken = this.closest('form').querySelector('[name="csrf_token"]').value;
        let productId = this.closest('form').querySelector('[name="product_id"]').value;
        console.log(productId)
        // Send updated quantity to the backend using AJAX
        updateQuantityInBackend(productId, newQuantity, csrfToken);
    });
});

// Function to update the quantity in the backend
function updateQuantityInBackend(productID, quantity, csrfToken) {
    fetch('/update-quantity', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken  
        },
        body: JSON.stringify({ product_id: productID, quantity: quantity })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            console.log(data.message);  // Log success message
        } else {
            console.error(data.message);  // Log error message
        }
    })
    .catch(error => console.error('Error:', error));  // Log any errors
}

