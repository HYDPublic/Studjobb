<?php
class Board {

    public function index () {
        $app = \Slim\Slim::getInstance();

        $jobs = Job::where('published', '=', 1)->take(10)->get();

        $app->render('static/header.php');
        $app->render('board.php', array ('jobs' => $jobs));
        $app->render('static/footer.php');
    }

    public function job ($id) {
        $app = \Slim\Slim::getInstance();

        $job = Job::find((int) $id);
        if (!$job || !$job->published)
            throw new Exception ('Fant ingen stilling.');

        $app->render('static/header.php');
        $app->render('job.php', array ('job' => $job));
        $app->render('static/footer.php');

    }
}
