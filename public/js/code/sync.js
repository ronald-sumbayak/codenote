var uri, token, timer, lastupdate = "0000-00-00 00:00:00";
setInterval (update, 1024);

$('#sourceCode').keydown (function () {
    clearTimeout (timer);
    timer = setTimeout (postData, 1024);
});

$('#input').keydown (function () {
    clearTimeout (timer);
    timer = setTimeout (postData, 1024);
});

function postData () {
    $.post ('/api/postdata', {
        'uri': uri,
        'source': $('#sourceCode').val (),
        'input': $('#input').val ()
    });
    lastupdate = new Date ();
}

function update () {
    $.get ('/api/getdata', {
        'uri': uri,
        'lastupdate': lastupdate
    }, function (data) {
        if (data['status'] === 'update') {
            $('#sourceCode').val (data['code']['source']);
            $('#input').val (data['code']['input']);
            lastupdate = data['code']['updated_at'];
        }
    });
}
