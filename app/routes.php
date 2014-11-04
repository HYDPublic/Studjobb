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
 * Newsletter
 */
$app->post('/nyhetsbrev', '\Newsletter:signup');

$app->get('/takk', '\Newsletter:thanks');

/**
 * Admin
 */
$app->get('/admin',                                              '\Admin:login');

$app->post('/admin',                                             '\Admin:authenticate');

$app->get('/admin/dashbord',      '\Admin::mustBeAuthenticated', '\Admin:dashboard');

// CrawledJob
$app->get('/admin/skrapt/:id',         '\Admin::mustBeAuthenticated', '\Admin:crawledJob');

$app->post('/admin/skrapt/:id/status', '\Admin::mustBeAuthenticated', '\Admin:updateCrawledJob');


// Job
$app->get('/admin/stilling/:id',  '\Admin::mustBeAuthenticated', '\Admin:job');

$app->post('/admin/stilling/:id', '\Admin::mustBeAuthenticated', '\Admin:updateJob');

$app->post('/admin/stilling',     '\Admin::mustBeAuthenticated', '\Admin:createJob');

// Company
$app->get('/admin/selskap/:id',   '\Admin::mustBeAuthenticated', '\Admin:company');

$app->post('/admin/selskap/:id',  '\Admin::mustBeAuthenticated', '\Admin:updateCompany');

/**
 * Mail
 */
$app->post('/admin/mail', '\Admin::mustBeAuthenticated', '\Mail:send');

/**
 * Errors
 */
$app->error('\Home::error');
