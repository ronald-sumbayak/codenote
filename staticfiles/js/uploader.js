let MAX_UPLOAD_SIZE = 2 * 1000 * 1000;  // 2 MB
let receivedFile;

let uploader = $('.uploader');
let uploaderTrigger = $('.uploader-trigger');
let uploaderControl = $('.uploader-control');
let uploaderURI = $('.uploader-uri');

function removeFile () {
    receivedFile = null;
    setHint ('idle', 'File removed', 'File removed');
    uploaderControl.hide ();
    uploaderURI.val ('');
    tooltips.tooltip ('hide');
}

function executeUpload () {
    let data = new FormData ();
    if (uploaderURI.val ().length > 0)
        data.append ('uri', uploaderURI.val ());
    data.append ('file', receivedFile);
    
    $.ajax ({
        url: endpoints.upload_api,
        type: 'POST',
        data: data,
        processData: false,
        contentType: false,
        success: data => {
            setHint (
                'success',
                `Upload complete. Directing to ${data.uri}...`,
                'Complete',
                'check');
            location.replace (`/${data.uri}`);
        },
        error: () => {
            setHint ('error', 'Upload failed');
            uploaderControl.prop ('disabled', false);
            enableUploader ();
        }
    });
}

function uploadFile () {
    setHint ('valid', 'Uploading');
    tooltips.tooltip ('hide');
    disableUploader ();
    uploaderControl.prop ('disabled', true);
    uploaderURI.removeClass ('is-invalid is-valid');
    if (uploaderURI.val ().length > 0) {
        $.post (endpoints.check, {uri: uploaderURI.val ()}, data => {
            uploaderURI.addClass ('is-valid');
            executeUpload (data.uri);
        }).fail (response => {
            uploaderControl.prop ('disabled', false);
            enableUploader ();
            setHint ('error', 'Can not connect to upload server.');
            /** @namespace response.responseJSON **/
            if (response.responseJSON.hasOwnProperty ('uri'))
                uploaderURI
                    .addClass ('is-invalid')
                    .parent ()
                    .find ('.invalid-feedback')
                    .html (response.responseJSON['uri']);
        });
    }
    else
        executeUpload ();
}

function setHint (type, status, text, icon) {
    if (status !== null)
        $('.uploader-status').html (text);
    if (text !== null)
        $('.uploader-text').html (text);
    if (icon !== null)
        $('.uploader-icon').html (icon);
    if (type !== null)
        $('.uploader-hint')
            .removeClass ('highlight valid error success idle')
            .addClass (type);
}

function setFile (file) {
    let filenameLimit = 25;
    let trimmed = file.name;
    if (trimmed.length > filenameLimit) {
        // display only first 'filenameLimit' file name
        let ext = trimmed.lastIndexOf ('.');
        let trim = filenameLimit - (trimmed.length - ext - 3);
        trimmed = trimmed.slice (0, trim) + '...' + trimmed.slice (ext);
    }
    
    receivedFile = file;
    uploaderControl.show ();
    setHint ('valid', file.name, trimmed, 'insert_drive_file');
}

function handleFiles (files) {
    receivedFile = null;

    if (files.length > 1)
        return setHint ('error', 'Can only upload one file');

    if (files[0].size > MAX_UPLOAD_SIZE)
        return setHint ('error', 'Maximum file size is 2MB');

    setFile (files[0]);
}

function enableUploader () {
    uploader.addClass ('uploader-hint');
    
    /** @namespace uploaderTrigger.children **/
    uploaderTrigger
        .on ('click', () => $('.uploader-file').trigger ('click'))
        .children ().on ('click', e => e.stopPropagation ());

    for (const type of ['dragenter', 'dragover', 'dragleave', 'drop'])
        uploader.on (type, preventDefault);

    for (const type of ['dragenter', 'dragover']) {
        uploader.on (type, () => {
            uploaderURI.removeClass ('is-invalid is-valid');
            uploaderControl.hide ();
            setHint ('highlight', null, 'Drop your file here', 'file_download');
        });
    }

    for (const type of ['dragleave', 'drop'])
        uploader.on (type, () => setHint ('idle', null, 'Drag your file here', null));

    uploader.on ('dragleave', () => {
        if (receivedFile != null)
            setFile (receivedFile);
    });

    uploader.on ('drop', e => {
        handleFiles (e.originalEvent.dataTransfer.files);
        uploaderControl.show ();
    });
}

function disableUploader () {
    for (const type of ['dragenter', 'dragover', 'dragleave', 'drop'])
        uploader.off (type);
    uploaderTrigger.off ('click');
}

function preventDefault (e) {
    e.preventDefault ();
    e.stopPropagation ();
}

$(document).ready (() => {
    $('.uploader-form').submit (e => {
        e.preventDefault ();
        uploadFile ();
    });

    for (const type of ['dragenter', 'dragover', 'dragleave', 'drop'])
        $('body').on (type, preventDefault);
    enableUploader ();
});
