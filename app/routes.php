<?php

/**
 * General pages
 */
$app->get('/om',      '\Home:about');

$app->get('/kontakt', '\Home:contact');

$app->get('/priser',  '\Home:pricing');

$app->notFound(function () use ($app) {
    \Home::notFound();
});

/**
 * Job board
 */
$app->get('/',             '\Board:index');

$app->get('/stilling/:id', '\Board:job');
