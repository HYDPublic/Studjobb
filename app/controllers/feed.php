<?php
class Feed {

    public function latestJobs () {
        $app = \Slim\Slim::getInstance();

        $app->response->headers->set('Content-Type', 'text/xml');
        $jobs = Job::where('published', true)->get();
        $app->render('feed.php', array (
            'jobs' => $jobs
        ));
    }
}
