document.addEventListener('DOMContentLoaded', function() {
    // Select all accordion toggle buttons on the order history page
    const accordionToggles = document.querySelectorAll('.accordion-toggle');

    accordionToggles.forEach(function(toggle) {
        // Get the selector for the collapse element this toggle controls
        const collapseSelector = toggle.getAttribute('data-bs-target');
        const collapseElement = document.querySelector(collapseSelector);

        // Skip if the collapse element is not found
        if (!collapseElement) return;

        // When the accordion section is shown, update the icon and label
        collapseElement.addEventListener('show.bs.collapse', function() {
            const icon = toggle.querySelector('i');
            const label = toggle.querySelector('.toggle-label');
            if (icon) {
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            }
            if (label) {
                label.textContent = 'Hide Details';
            }
        });

        // When the accordion section is hidden, revert the icon and label
        collapseElement.addEventListener('hide.bs.collapse', function() {
            const icon = toggle.querySelector('i');
            const label = toggle.querySelector('.toggle-label');
            if (icon) {
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            }
            if (label) {
                label.textContent = 'View Details';
            }
        });
    });

    // Address delete modal logic for saved addresses page
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const modalElement = document.getElementById('deleteModal');
    const confirmBtn = document.getElementById('confirmDeleteBtn');
    const addressNameElement = document.getElementById('addressName');

    if (deleteButtons.length && modalElement && confirmBtn && addressNameElement) {
        const modal = new bootstrap.Modal(modalElement);

     deleteButtons.forEach(button => {
            button.addEventListener('click', function() {
                const addressId = this.getAttribute('data-address-id');
                const addressName = this.getAttribute('data-address-name');

                addressNameElement.textContent = addressName;
                modal.show();

                confirmBtn.onclick = function() {
                    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                    fetch('/accounts/addresses/' + addressId + '/delete/', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrfToken
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            location.reload();
                        } else {
                            alert('Error: ' + data.message);
                        }
                        modal.hide();
                    })   
                    .catch(error => {
                        console.error('Error:', error);
                        alert('Error deleting address. Please try again.');
                        modal.hide();
                    });
                };
            });
        });
    }
});