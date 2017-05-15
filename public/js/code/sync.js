var uri, caret, token, timer, lastupdate = "0000-00-00 00:00:00";
setInterval (update, 1024);

$('#sourceCode').keydown (function () {
    clearTimeout (timer);
    timer = setTimeout (postData, 1729);
});

$('#input').keydown (function () {
    clearTimeout (timer);
    timer = setTimeout (postData, 1024);
});

function postData () {
    $.get ('/api/postdata/', {
        'uri': uri,
        'caret': $('#sourceCode').prop ('selectionStart'),
        'source': $('#sourceCode').val (),
        'input': $('#input').val ()
    });

    caret = $('#sourceCode').prop ('selectionStart');
}

function update () {
    $.get ('/api/getdata/', {
        'uri': uri,
        'lastupdate': lastupdate
    }, function (data) {
        if (data['status'] == 'update') {
            $('#sourceCode').val (data['code']['source']);
            $('#sourceCode').prop ('selectionStart', data['code']['caret']);
            $('#sourceCode').prop ('selectionEnd', data['code']['caret']);
            $('#input').val (data['code']['input']);
            $('#lang').val (data['code']['langId']);
            lastupdate = data['code']['updated_at'];
        }
    });
}
