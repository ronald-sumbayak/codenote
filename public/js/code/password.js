$('#open-password').click (function () {
    if ($('#password-form').is (':visible')) $('#password-form').hide ();
    else $('#password-form').show ();
});

function check_password () {
    $('#checkpassword-alert').hide ();
    $.ajax ({
        url: '/api/checkpassword/',
        type: 'POST',
        data: {
            'uri': uri,
            'password': $('#password').val ()
        },
        success: function (data) {
            if (data['status'] == 'success')
                window.location.reload (true);
            else {
                $('#checkpassword-alert').html (data['status']);
                $('#checkpassword-alert').show ();
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#checkpassword-alert').html (errorThrown);
            $('#checkpassword-alert').show ();
        }
    });
}

function change_password () {
    $('#setpassword-alert').hide ();
    console.log ('setpassword');
    $.ajax ({
        url: '/api/setpassword/',
        type: 'POST',
        data: {
            'uri': uri,
            'oldpassword': $('#old-password').val (),
            'newpassword': $('#new-password').val ()
        },
        success: function (data) {
            console.log (data);
            if (data['status'] == 'success')
                // if ($('#old-password').val () != $('#new-password').val ())
                window.location.replace ("/" + uri);
            else {
                $('#setpassword-alert').html (data['status']);
                $('#setpassword-alert').show ();
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#setpassword-alert').html (errorThrown);
            $('#setpassword-alert').show ();
        }
    });
}

function clear_password () {
    $.ajax ({
        url: '/api/clearpassword/',
        type: 'POST',
        data: { 'uri': uri },
        success: function (data) {
            if (data['status'] == 'success')
                window.location.replace (uri);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#setpassword-alert').html (errorThrown);
            $('#setpassword-alert').show ();
        }
    });
}
