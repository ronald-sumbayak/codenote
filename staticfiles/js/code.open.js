let codePassword = $('.code-password');
let codeURI = $('.code-uri');

$(document).ready (() => {
    let headerPassword = $('.code-header.code-password');
    let formPassword = $('.code-form.code-password');
    
    let passwordFocus;
    if (password) {
        $('#password-unlocked').parent ().hide ();
        passwordFocus = '#password-locked';
    }
    else {
        $('#password-locked').parent ().hide ();
        passwordFocus = '#password-unlocked';
    }
    
    headerPassword.magnificPopup ({
        type: 'inline',
        focus: passwordFocus,
        closeOnBgClick: false
    });
    
    $('.code-header.code-uri').magnificPopup ({
        type: 'inline',
        focus: '.code-uri',
        closeOnBgClick: false
    });
    
    formPassword.submit (e => {
        e.preventDefault ();
        tooltips.tooltip ('hide');
        let inputPassword = $(e.target).find ('.code-input');
        inputPassword.removeClass ('is-invalid');
        codePassword.prop ('disabled', true);

        $.post (endpoints.lock, {uri: uri, password: inputPassword.val ()}, () => {
            $.magnificPopup.close ();
            headerPassword.magnificPopup ({
                type: 'inline',
                focus: '#password-locked',
                closeOnBgClick: false
            });
            formPassword.toggle ();
            inputPassword.val ('');
            codePassword.prop ('disabled', false);
        }).fail (response => {
            /** @namespace response.responseJSON **/
            if (response.responseJSON.hasOwnProperty ('password'))
                inputPassword
                    .addClass ('is-invalid')
                    .parent ()
                    .find ('.invalid-feedback')
                    .html (response.responseJSON['password'][0]);
            codePassword.prop ('disabled', false);
        });
    });
    
    $('.code-password.code-unlock').click (() => {
        tooltips.tooltip ('hide');
        let inputPassword = $('.code-input.code-password');
        inputPassword.removeClass ('is-invalid');
        codePassword.prop ('disabled', true);
        
        $.post (endpoints.unlock, {uri: uri}, () => {
            $.magnificPopup.close ();
            headerPassword.magnificPopup ({
                type: 'inline',
                focus: '#password-unlocked',
                closeOnBgClick: false
            });
            formPassword.toggle ();
            inputPassword.val ('');
            codePassword.prop ('disabled', false);
        });
    });
    
    $('.code-form.code-uri').submit (e => {
        e.preventDefault ();
        tooltips.tooltip ('hide');
        let inputURI = $(e.target).find ('.code-input');
        inputURI.removeClass ('is-invalid');
        codeURI.prop ('disabled', true);

        $.post (endpoints.rename, {uri: uri, new_uri: inputURI.val ()}, data => {
            location.replace (`/${data.uri}`);
        }).fail (response => {
            /** @namespace response.responseJSON **/
            if (response.responseJSON.hasOwnProperty ('new_uri'))
                inputURI
                    .addClass ('is-invalid')
                    .parent ()
                    .find ('.invalid-feedback')
                    .html (response.responseJSON['new_uri']);
            codeURI.prop ('disabled', false);
        });
    });
    
});
