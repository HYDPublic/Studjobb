<?php
class Board {

    public function index () {
        $app = \Slim\Slim::getInstance();

        $categories = Category::whereHas('jobs', function ($q) {
            $q->where('published', 1);
        })->get();

        $app->render('static/header.php');
        $app->render('board.php', array ('categories' => $categories));
        $app->render('static/footer.php');
    }

    public function job ($id) {
        $app = \Slim\Slim::getInstance();

        $job = Job::find($id);

        if (!$job || !$job->published)
            throw new Exception ('Fant ingen stilling.');

        $app->render('static/header.php');
        $app->render('job.php', array ('job' => $job));
        $app->render('static/footer.php');

    }
}
