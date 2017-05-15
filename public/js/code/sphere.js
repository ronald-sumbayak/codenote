function retrieveLanguage () {
    $.ajax ({
        url: 'http://2fd2a00c.compilers.sphere-engine.com/api/v3/languages',
        data: { 'access_token': token },
        dataType: 'json',
        success: function (data) {
            for (var key in data)
                $('#lang').append ("<option value=\"" + key + "\">" + data[key] + "</option>");
            update ();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            retrieveLanguage ();
        }
    });
}

function retrieveToken () {
    $.ajax ({
        url: '/api/token',
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
