var uri, caret, token, lastupdate;

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

$('#open-password').click (function () {
    if ($('#password-form').is (':visible')) $('#password-form').hide ();
    else $('#password-form').show ();
});

function change_password () {
    $('#setpassword-alert').hide ();
    $.ajax ({
        url: '/api/setpassword/',
        type: 'POST',
        data: {
            'uri': uri,
            'oldpassword': $('#old-password').val (),
            'newpassword': $('#new-password').val ()
        },
        success: function (data) {
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
        data: {
            'uri': uri
        },
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

function changeuri () {
    $('#changeuri-alert').hide ();
    if ($('#new-uri').val () != uri) {
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
}

$('#open-changeuri').click (function () {
    if ($('#changeuri-form').is (':visible')) $('#changeuri-form').hide ();
    else $('#changeuri-form').show ();
});


function retrieveLanguage () {
    $.ajax ({
        url: 'http://2fd2a00c.compilers.sphere-engine.com/api/v3/languages',
        data: {
            'access_token': token
        },
        dataType: 'json',
        success: function (data) {
            for (var key in data)
                $('#lang').append ("<option value=\"" + key + "\">" + data[key] + "</option>");
        },
        error: function (jqXHR, textStatus, errorThrown) {
            retrieveLanguage ();
        }
    });
}

function retrieveToken () {
    $.ajax ({
        url: '/api/token/',
        success: function (data) {
            token = data;
            retrieveLanguage ();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            retrieveToken ();
        }
    });
}

$(document).ready (retrieveToken ());
var submit = 'http://2fd2a00c.compilers.sphere-engine.com/api/v3/submissions';

function hideLoading () {
    $('.code-form').prop ('disabled', false);
}

function postResult (data) {
    $.post ('/api/submission/', { 'id': data['id'] });

    $.post ('/api/putdata/', {
        'uri': uri,
        'caret': 0,
        'compiled': 1,
        'langid': data['langId'],
        'language': data['langName'],
        'compiler': data['langVersion'],
        'time': data['time'],
        'result': data['result'],
        'memory': data['result'],
        'code': $('#sourceCode').val (),
        'input': $('#input').val (),
        'output': data['output']
    });
}

function displayResult (data) {
    postResult (data);

    if (data['result'] == 15) {
        $('#success-alert').html ("Success! time:" + data['time'] + " memory:" + data['memory']);
        $('#success-alert').show ();
        $('#output').html (data['output']);
        $('#output').show ();
    }
    else {
        var errorText;
        if (data['result'] == 11) {
            errorText = "compilation error";
            $('#cmpinfo-alert').html (data['cmpinfo'].replace ('\n', "<br>"));
            $('#cmpinfo-alert').show ();
        }
        else if (data['result'] == 12) {
            errorText = "runtime error! " + "signal:" + data['signal'];
            $('#stderr-alert').html (data['stderr'].replace ('\n', "<br>"));
            $('#stderr-alert').show ();
        }

        else if (data['result'] == 13) errorText = 'time limit exceeded ' + data['time'];
        else if (data['result'] == 17) errorText = 'memory limit exceeded ' + data['memory'];
        else if (data['result'] == 19) errorText = 'illegal system call';
        else if (data['result'] == 20) errorText = 'internal error';

        $('#error-alert').html (errorText);
        $('#error-alert').show ();
    }

    hideLoading ();
}

function retrieveResult (id) {
    $.ajax ({
        url: submit + '/' + id,
        data: {
            'access_token': token,
            'withOutput': true,
            'withStderr': true,
            'withCmpinfo': true
        },
        success: function (data) {
            data = [data.slice (0, 1), "\"id\":", id, ",", data.slice (1)].join ('');

            $.post ('/api/convert/', { 'text': data }, function (convert) {
                if (convert['error'] != "OK") {
                    $('#error-alert').html (convert['error']);
                    $('#error-alert').show ();
                    hideLoading ();
                }
                else {
                    var status;
                    if (convert['status'] < 0) status = "waiting...";
                    else if (convert['status'] == 0) status = "Run";
                    else if (convert['status'] == 1) status = "compiling...";
                    else if (convert['status'] == 3) status = "running...";

                    $('#run').html (status);
                    if (convert['status'] == 0) displayResult (convert);
                    else retrieveResult (convert['id']);
                }
            }, 'json');
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#error-alert').html (errorThrown);
            $('#error-alert').show ();
            hideLoading ();
        }
    });
}

function showLoading () {
    $('.code-form').prop ('disabled', true);
    $('.compilation-alert').hide ();
    $('#output').empty ();
    $('#output').hide ();
}

function run () {
    showLoading ();

    $.ajax ({
        url: submit + '?access_token=' + token,
        type: 'POST',
        data: {
            'sourceCode': $('#sourceCode').val (),
            'language': $('#lang').val (),
            'input': $('#input').val ()
        },
        dataType: 'json',
        success: function (data) {
            retrieveResult (data['id']);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#error-alert').html (errorThrown);
            $('#error-alert').show ();
            hideLoading ();
        }
    });
}

var updater;

$(document).ready (function () {
    updater = setInterval (update, 3000);
});

function update () {
    caret = $('#sourceCode').prop ('selectionStart');

    $.get ('/api/getdata/', { 'uri': uri }, function (data) {
        $('#sourceCode').val (data['code']);
        $('#input').val (data['input']);
        $('#lang').val (data['langId']);
    });
}

$(document).delegate ('#sourceCode', 'keydown', function (e) {
    var keyCode = e.keyCode || e.which;

    if (keyCode == 9) {
        e.preventDefault ();
        var start = $(this).get (0).selectionStart;
        var end = $(this).get (0).selectionEnd;

        $(this).val ($(this).val ().substring (0, start) + "    " + $(this).val ().substring (end));
        $(this).get (0).selectionStart = $(this).get (0).selectionEnd = start + 4;
    }
});
