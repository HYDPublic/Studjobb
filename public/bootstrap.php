<?php
require '../vendor/autoload.php';
require '../app/configuration.php';

/**
 * Slim
 */
$app = new \Slim\Slim();

/**
 * Routing
 */
require '../app/routes.php';

/**
 * Eloquent
 */
$connectionFactory = new \Illuminate\Database\Connectors\ConnectionFactory();
$connection        = $connFactory->make($configuration['database']);

$resolver          = new \Illuminate\Database\ConnectionResolver();
$resolver->addConnection('default', $connection);
$resolver->setDefaultConnection('default');
\Illuminate\Database\Eloquent\Model::setConnectionResolver($resolver);

/**
 * Take-off
 */
$app->run();
