$(document).ready(function () {
    $('tr').on("click", function() {
        if ($(this).data('href') !== undefined)
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

    $('form#submit').submit(function (event) {
        $('textarea#buffer').val(editor.getHTML());
        return true;
    });

    if ($.cookie('newsletter') !== 'seen') {
        setTimeout(function () {
            $('#newsletter').modal('show');
            $.cookie('newsletter', 'seen', {
                expires: 60,
                path: '/'
            });
        }, 4000);
    }

    var seconds = 0;
    $('#newsletter').on('show.bs.modal', function () {
        setInterval(function () {
            seconds++;
        }, 1000);
        _paq.push(['trackEvent', 'Modal', 'Open']);
    });

    $('#newsletter').on('hidden.bs.modal', function () {
        _paq.push(['trackEvent', 'Modal', 'Closed', 'Time', seconds]);
    });

    $('form#update-job').submit(function (event) {
        $('textarea#buffer').val(editor.getHTML());
        return true;
    });
});
