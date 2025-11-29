/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    
*/

// Initialize Stripe with public key from template
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Custom styling for Stripe elements (match bootstrap form styles)
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create and mount card element
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors from the card Element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit and payment processing
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
    // Disable submit button to prevent multiple submissions
    card.update({ 'disabled': true});
    document.getElementById('submit-button').disabled = true;
    document.getElementById('button-text').classList.add('d-none');
    document.getElementById('loading').classList.remove('d-none');
    
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                email: form.email.value.trim(),
                address: {
                    line1: form.street_address_1.value.trim(),
                    line2: form.street_address_2.value.trim(),
                    city: form.city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                }
            }
        }
    }).then(function(result) {
        if (result.error) {
            // Payment failed - display error message and re-enable form
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            errorDiv.innerHTML = html;
            
            // Re-enable form for resubmission
            card.update({ 'disabled': false});
            document.getElementById('submit-button').disabled = false;
            document.getElementById('button-text').classList.remove('d-none');
            document.getElementById('loading').classList.add('d-none');
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});