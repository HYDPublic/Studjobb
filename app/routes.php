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

$app->get('/utlys',        '\Board:submit');

$app->post('/utlys',       '\Board:submitJob');

$app->get('/finn',        '\Board:search');

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
 * Feed
 */
$app->get('/rss', '\Feed:latestJobs');

/**
 * Deploy
 */
$app->post('/deploy', '\Deploy:pull');

/**
 * Errors
 */
$app->error('\Home::error');
