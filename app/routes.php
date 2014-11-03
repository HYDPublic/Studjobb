<?php

/**
 * General pages
 */
$app->get('/om',      '\Home:about');

$app->get('/kontakt', '\Home:contact');

$app->get('/priser',  '\Home:pricing');

$app->notFound(       '\Home::notFound');

/**
 * Job board
 */
$app->get('/',             '\Board:index');

$app->get('/stilling/:id', '\Board:job');

/**
 * Admin
 */
$app->get('/admin', '\Admin:login');

$app->post('/admin', '\Admin:authenticate');

/**
 * Errors
 */
$app->error(function(\Exception $e) use ($app) {
    print_r($e->getMessage());
});
