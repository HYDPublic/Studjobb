<?php
require __DIR__.'/../vendor/autoload.php';
require __DIR__.'/configuration.php';

/**
 * Timezone
 */
date_default_timezone_set('Europe/Oslo');

/**
 * Slim
 */
$app = new \Slim\Slim();
$app->config($configuration['slim']);

/**
 * Mailchimp
 */
$app->mailchimp = new \Drewm\MailChimp($configuration['mailchimp']['key']);

/**
 * Mail
 */
$app->mailconfig = $configuration['mail'];

/**
 * Piwik
 */
$app->piwik = $configuration['piwik'];

/**
 * Logo
 */
$app->logo = $configuration['logo']; 

/**
 * Controllers
 */
foreach (glob(__DIR__.'/controllers/*.php') as $controller)
    require_once $controller;

/**
 * Models
 */
foreach (glob(__DIR__.'/models/*.php') as $model)
   require_once $model;

/**
 * Routing
 */
require __DIR__.'/routes.php';

/**
 * Sentry
 */
class_alias('Cartalyst\Sentry\Facades\Native\Sentry', 'Sentry');

/**
 * Eloquent
 */
use Illuminate\Database\Capsule\Manager as Capsule;
use Illuminate\Events\Dispatcher;
use Illuminate\Container\Container;

$capsule = new Capsule;
$capsule->addConnection($configuration['database']);

$capsule->setEventDispatcher(new Dispatcher(new Container));
$capsule->setAsGlobal();
$capsule->bootEloquent();

/**
 * Take-off
 */
$app->run();
