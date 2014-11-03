<?php
class Board {

    public function index () {
        $app = \Slim\Slim::getInstance();

        $jobs = Job::where('published', '=', 1)->take(10)->get();

        $app->render('header.php');
        $app->render('board.php', array ('jobs' => $jobs));
        $app->render('footer.php');
    }

    public function job ($id) {
        $app = \Slim\Slim::getInstance();

        $job = Job::find((int) $id);
        if (!$job || !$job->published)
            throw new Exception ('Fant ingen stilling.');

        $app->render('header.php');
        $app->render('job.php', array ('job' => $job));
        $app->render('footer.php');

    }
}
