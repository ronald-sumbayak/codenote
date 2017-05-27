$('#open-input').click (function () {
    $('#input').slideToggle ();
});

var prev = 0;

$('#lang').on ('change', function () {
    console.log ($(this).val ());
    if ($(this).val () == 0) $('#compile-button').slideUp ();
    else if (prev == 0) $('#compile-button').slideDown ();
    prev = $(this).val ();
});