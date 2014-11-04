<?php
class Feed {

    public function latestJobs () {
        $app = \Slim\Slim::getInstance();

        $app->response->headers->set('Content-Type', 'text/xml');

    }
}
