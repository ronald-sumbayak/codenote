$('#clear-password').click (function () {
    $('#setpassword-alert').empty ().hide ();
    $.post ('/api/clearpassword', {'uri': uri}, function (data) {
        console.log (data);
        if (data['status'] === 'success')
            window.location.replace (uri);
    });

    return false;
});

$('#set-password').click (function () {
    $('#setpassword-alert').empty ().hide ();
    $.ajax ({
        url: '/api/setpassword',
        type: 'POST',
        headers: { 'X-CSRF-TOKEN': token },
        data: {
            'uri'        : uri,
            'oldpassword': $('#old-password').val (),
            'newpassword': $('#new-password').val ()
        },
        success: function (data) {
            if (data['status'] === 'success')
                window.location.replace ("/" + uri);
            else
                $('#set-password-alert').html (data['status']).show ();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#set-password-alert').html (errorThrown).show ();
        }
    });

    return false;
});

$('#check-password').click (function () {
    $('#checkpassword-alert').empty ().hide ();
    $.ajax ({
        url: '/api/checkpassword',
        type: 'POST',
        data: {
            'uri'     : uri,
            'password': $('#password').val ()
        },
        success: function (data) {
            if (data['status'] === 'success')
                window.location.reload (true);
            else
                $('#checkpassword-alert').html (data['status']).show ();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#checkpassword-alert').html (errorThrown).show ();
        }
    });

    return false;
});
