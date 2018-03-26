let cm;
let dmp = new diff_match_patch ();
let clock;

function makePatches (diffs) {
    let patches = [];
    let cursor = 0;
    
    for (const diff of diffs) {
        switch (diff[0]) {
            case 0:
                cursor += diff[1].length;
                break;
            case -1:
                patches.push ([diff[0], cursor, diff[1].length]);
                break;
            case 1:
                patches.push ([diff[0], cursor, diff[1]]);
                cursor += diff[1].length;
                break;
        }
    }
    return patches;
}

function sendDiff () {
    let diffs = dmp.diff_main (code.source, cm.getValue ());
    dmp.diff_cleanupEfficiency (diffs);
    let patches = makePatches (diffs);
    
    let data = new FormData ();
    data.append ('uri', code.uri);
    data.append ('version', code.version);
    data.append ('patches', patches);
    
    $.post (endpoints.update, {uri: code.uri, version: code.version, patches: JSON.stringify (patches)}, data => {
        code.source = data.source;
    });
}

$(document).ready (() => {
    cm = CodeMirror.fromTextArea ($('.code-editor')[0], {
        lineNumbers : true,
        indentUnit: 4,
        matchBrackets: true,
        styleActiveLine: {
            nonEmpty: true
        }
    });
    
    $.post (endpoints.code, {uri: uri}, data => {
        code = data;
        cm.setValue (data.source);
        cm.on ('change', () => {
            clearTimeout (clock);
            clock = setTimeout (sendDiff, 1729);
        });
        ideCompiler.val (code.language);
    })
});
