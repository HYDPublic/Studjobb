$(document).ready(function () {
    $('tr').on("click", function() {
        document.location = $(this).data('href');
    });

    jQuery.timeago.settings.allowFuture = true;
    $('td.timeago').timeago();

    if ($('#editor-container').length > 0) {
        var editor = new Quill('#editor-container', {
            modules: {
              'toolbar': {
                  container: '#formatting-container'
              },
              'image-tooltip': true,
              'link-tooltip': true
            }
        });
    }

    if ($.cookie('newsletter') !== 'seen') {
        setTimeout(function () {
            $('#newsletter').modal('show');
            $.cookie('newsletter', 'seen', {
                expires: 60,
                path: '/'
            });
        }, 5000);
    }
    
    $('form#update-job').submit(function (event) {
        $('textarea#buffer').val(editor.getHTML());
        return true;
    });
});
