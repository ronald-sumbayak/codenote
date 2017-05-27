$('#login').click (function (e) {
    console.log ("login");
    $('#login-alert').hide ();
    $.ajax ({
        url: '/login',
        type: 'post',
        dataType: 'json',
        data: {
            'email': $('#email').val (),
            'password': $('#password').val ()
        },
        success: function (data) {
            if (data['status'] === 'success')
                window.location.replace ("/" + uri);
            else
                $('#login-alert').html (data['status']).show ();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#login-alert').html (data['status']).show ();
        }
    });

    return false;
});