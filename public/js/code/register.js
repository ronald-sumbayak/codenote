$('#register').click (function () {
    $('#register-alert').empty ().hide ();
    console.log ('register');

    $.ajax ({
        url: '/register',
        type: 'POST',
        data: {
            'name': $('#name').val (),
            'email': $('#email').val (),
            'password': $('#password').val (),
            'password_confirmation': $('#password-confirm').val ()
        },
        success: function (data) {
            if (data['status'] === "success")
                window.location.replace ("/");
            else
                $('#register-alert').html (data['status']).show ();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#register-alert').html (errorThrown).show ();
        }
    });

    return false;
});