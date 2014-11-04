$(document).ready(function () {
    $('tr').on("click", function() {
        document.location = $(this).data('href');
    });

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

    $('form#update-job').submit(function (event) {
        $('textarea#buffer').val(editor.getHTML());
        return true;
    });
});
