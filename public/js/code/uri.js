$('#changeuri').click (function () {
    $('#changeuri-alert').hide ();

    $.post ('/api/changeuri', {
        'uri': uri,
        'newuri': $('#new-uri').val ()
    }, function (data) {
        if (data['status'] === 'success')
            window.location.replace ("/" + $('#new-uri').val ());
        else
            $('#changeuri-alert').html (data['status']).show ();
    });
    return false;
});

$('#new-uri').keyup (function () {
    var newuri = $('#new-uri').val ();
    if (newuri === uri || newuri.length === 0)
        $('#changeuri').prop ('disabled', true);
    else
        $('#changeuri').prop ('disabled', false);
});