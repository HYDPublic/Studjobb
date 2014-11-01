<?php
require '../vendor/autoload.php';
require '../app/configuration.php';

/**
 * Slim
 */
$app = new \Slim\Slim();

/**
 * Controllers
 */
foreach (glob('../app/controllers/*.php') as $controller)
    require_once $controller;

/**
 * Routing
 */
require '../app/routes.php';

/**
 * Eloquent
 */
use Illuminate\Database\Capsule\Manager as Capsule;
use Illuminate\Events\Dispatcher;
use Illuminate\Container\Container;

$capsule = new Capsule;
$capsule->addConnection([
    $configuration['database']
]);

$capsule->setEventDispatcher(new Dispatcher(new Container));
$capsule->bootEloquent();

/**
 * Take-off
 */
$app->run();
