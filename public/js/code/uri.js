$('#open-changeuri').click (function () {
    if ($('#changeuri-form').is (':visible')) $('#changeuri-form').hide ();
    else $('#changeuri-form').show ();
});

function changeuri () {
    $('#changeuri-alert').hide ();
    if ($('#new-uri').val () == uri) return;

    $.ajax ({
        url: '/api/changeuri/',
        type: 'POST',
        data: {
            'uri': uri,
            'newuri': $('#new-uri').val ()
        },
        success: function (data) {
            if (data['status'] == 'success') {
                if ($('#new-uri').val () != uri)
                    window.location.replace ("/" + $('#new-uri').val ())
            }
            else {
                $('#changeuri-alert').html (data['status']);
                $('#changeuri-alert').show ();
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#changeuri-alert').html (errorThrown);
            $('#changeuri-alert').show ();
        }
    });
}
