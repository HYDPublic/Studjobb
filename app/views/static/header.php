<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Studjobb</title>
        <link rel="icon" type="image/png" href="/favicon.ico">
        <link rel="stylesheet" href="/css/bootstrap.min.css">
        <link rel="stylesheet" href="/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="/css/font-awesome.min.css" >
        <link rel="stylesheet" href="/css/style.css">
        <script src="/js/jquery.min.js"></script>
        <script src="/js/jquery.cookie.js"></script>
        <script src="/js/timeago.jquery.js"></script>
        <script src="/js/no-nb.timeago.js"></script>
        <script src="/js/bootstrap.min.js"></script>
        <script src="/js/quill.min.js"></script>
        <script src="/js/app.js"></script>
    </head>
    <body>
        <div id="header">
            <a href="/">
                <?php if (!strstr($_SERVER['REQUEST_URI'], 'stilling')): ?>
                <img src="/img/header.jpg">
                <?php else: ?>
                <img src="/img/header-small.jpg">
                <?php endif; ?>
            </a>
        </div>
        <div class="container">
