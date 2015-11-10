document.addEventListener('DOMContentLoaded', function () {
    logo_url_field = document.querySelector('input[name="logo"]');
    search_results = document.querySelectorAll('img.search-result');
    for (i = 0; i < search_results.length; i++) {
        search_result = search_results[i];
        search_result.addEventListener('click', function () {
            image_url = this.src;
            logo_url_field.value = image_url;
        });
    }
});
