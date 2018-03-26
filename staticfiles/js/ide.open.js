let ideCompiler = $('.ide-compiler');

$(document).ready (() => {
    ideCompiler.change (e => {
        let selection = $(e.target).find (':selected');
        let codemirror = selection.data ('codemirror');
        let mime = selection.data ('mime');
        
        $.post (endpoints.update, {uri: code.uri, version: code.version, language: selection.val ()}, data => {
            code = data;
        });
        
        $.getScript (`${endpoints.mode}/${codemirror}/${codemirror}.js`, () => {
            cm.setOption ('mode', mime);
            $('.compiler-btn')
                .prop ('disabled', false)
                .removeClass ('disabled');
        });
    });
});
