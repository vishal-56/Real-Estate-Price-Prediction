$(document).ready(function () {
    // Load locations
    $.ajax({
        url: 'http://127.0.0.1:5000/get_locations_name',
        method: 'GET',
        success: function (data) {
            let locations = data.locations;
            let $locationSelect = $('#location');
            $locationSelect.empty(); // Clear existing options
            locations.forEach(function (location) {
                $locationSelect.append($('<option></option>').val(location).text(location));
            });
        },
        error: function () {
            alert('Error: Unable to load locations.');
        }
    });

    // Handle form submission
    $('#price-form').on('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        let formData = {
            total_sqft: $('#total_sqft').val(),
            location: $('#location').val(),
            bhk: $('#bhk').val(),
            bath: $('#bath').val()
        };

        $.ajax({
            url: 'http://127.0.0.1:5000/predict_home_price',
            method: 'POST',
            data: formData,
            success: function (response) {
                $('#result').html(`<p>Estimated Price: ${response.estimated_price} Lakh</p>`);
            },
            error: function () {
                $('#result').html('<p>Error: Unable to get estimated price.</p>');
            }
        });
    });
});
