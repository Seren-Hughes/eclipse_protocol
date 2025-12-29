/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
*/

// Wait for DOM to be loaded before initializing
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Stripe with public key from template
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();

    // Custom styling for Stripe elements (match dark theme)
    var style = {
        base: {
            color: '#fff',
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
    var card = elements.create('card', {style: style, hidePostalCode: true});
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
        
        // Get the card name element safely
        var cardNameElement = document.getElementById('card-name');
        var cardName = cardNameElement ? cardNameElement.value.trim() : '';
        
        console.log('Form submitted');
        console.log('Card name:', cardName);
        console.log('Client Secret exists:', !!clientSecret);
        
        // Disable submit button to prevent multiple submissions
        card.update({ 'disabled': true});
        document.getElementById('submit-button').disabled = true;
        document.getElementById('button-text').classList.add('d-none');
        document.getElementById('loading').classList.remove('d-none');
        
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: cardName,
                }
            }
        }).then(function(result) {
            console.log('Stripe result:', result);
            
            if (result.error) {
                console.error('Payment error:', result.error);
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
                console.log('Payment Intent Status:', result.paymentIntent.status);
                if (result.paymentIntent.status === 'succeeded') {
                    console.log('Payment succeeded, submitting form');
                    form.submit();
                }
            }
        }).catch(function(error) {
            console.error('Stripe error:', error);
            
            // Display error to user
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>An unexpected error occurred. Please try again.</span>`;
            errorDiv.innerHTML = html;
            
            // Re-enable form
            card.update({ 'disabled': false});
            document.getElementById('submit-button').disabled = false;
            document.getElementById('button-text').classList.remove('d-none');
            document.getElementById('loading').classList.add('d-none');
        });
    });
});