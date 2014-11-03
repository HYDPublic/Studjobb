$(document).ready(function () {
    $('tr').on("click", function() {
        document.location = $(this).data('href');
    });
});
