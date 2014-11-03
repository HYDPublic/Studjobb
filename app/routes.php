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
$app->get('/admin',                                              '\Admin:login');

$app->post('/admin',                                             '\Admin:authenticate');

$app->get('/admin/dashbord',      '\Admin::mustBeAuthenticated', '\Admin:dashboard');

$app->get('/admin/stilling/:id',  '\Admin::mustBeAuthenticated', '\Admin:job');

$app->post('/admin/stilling/:id', '\Admin::mustBeAuthenticated', '\Admin:updateJob');

$app->get('/admin/skrapt/:id',    '\Admin::mustBeAuthenticated', '\Admin:crawledJob');


/**
 * Errors
 */
$app->error(function(\Exception $e) use ($app) {
    print_r($e->getMessage());
});
