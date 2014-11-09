<?php
class Board {

    public function index () {
        $app = \Slim\Slim::getInstance();

        $schools    = School::all();
        $categories = Category::whereHas('jobs', function ($q) {
            $q->where('published', '=', true);
        })->get();

        $app->render('static/header.php');
        $app->render('board.php', array (
            'categories' => $categories,
            'schools'    => $schools
        ));
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

    public function submit () {
        $app = \Slim\Slim::getInstance();

        $app->render('static/header.php');
        $app->render('submit/form.php');
        $app->render('static/footer.php');
    }

    public function submitJob () {
        $app = \Slim\Slim::getInstance();

        $app->render('static/header.php');
        $app->render('submit/thanks.php');
        $app->render('static/footer.php');
    }

    public function search () {
        $app = \Slim\Slim::getInstance();

        $schools  = School::all();
        $query    = $app->request->post('q');
        $jobs     = Job::where('content', 'like', '%'.$query.'%')->get();

        $app->render('static/header.php');
        $app->render('results.php', array (
            'jobs' => $jobs,
            'schools' => $schools
        ));
        $app->render('static/footer.php');
    }
}
