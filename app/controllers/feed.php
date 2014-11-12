<?php
class Feed {

    public function latestJobs () {
        $app = \Slim\Slim::getInstance();

        $app->response->headers->set('Content-Type', 'text/xml');
        $jobs = Job::where('published', true)
                ->whereRaw('created_at >= now() - interval 1 week')
                ->orderBy('created_at', 'DESC')
                ->get();
        $app->render('feed.php', array (
            'jobs' => $jobs
        ));
    }
}
