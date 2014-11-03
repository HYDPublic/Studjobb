<?php
class Board {

    public function index () {
        $app = \Slim\Slim::getInstance();
        $app->render('header.php');
        $app->render('board.php');
        $app->render('footer.php');
    }

    public function job ($id) {
        $app = \Slim\Slim::getInstance();

        $job = Job::find((int) $id);
        if (!$job)
            throw new Exception ('Fant ingen stilling.');

        $app->render('header.php');
        $app->render('job.php', array ('job' => $job));
        $app->render('footer.php');

    }
}
