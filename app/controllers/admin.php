<?php
class Admin {

    public function login () {
        $app = \Slim\Slim::getInstance();

        if (Sentry::check())
            $app->redirect('/admin/dashbord');

        $app->render('static/header.php');
        $app->render('admin/login.php');
        $app->render('static/footer.php');
    }

    public function job ($id) {
        $app = \Slim\Slim::getInstance();

        $job = Job::find((int) $id);
        if (!$job || !$job->published)
            throw new Exception ('Fant ingen stilling.');

        $app->render('static/header.php');
        $app->render('admin/edit-job.php', array ('job' => $job));
        $app->render('static/footer.php');
    }

    public function updateJob ($id) {
        $app = \Slim\Slim::getInstance();

        $job = Job::find($id);
        $job->title   = $app->request->post('title');
        $job->content = $app->request->post('content');
        $job->save();

        $app->redirect('/admin/stilling/' . $id);
    }

    public function crawledJob ($id) {
        $app = \Slim\Slim::getInstance();

        $crawledJob = CrawledJob::find((int) $id);
        if (!$crawledJob)
            throw new Exception ('Fant ingen skrapt jobb.');

        $app->render('static/header.php');
        $app->render('admin/edit-crawledJob.php', array (
            'crawledJob' => $crawledJob
        ));
        $app->render('static/footer.php');
    }

    public function authenticate () {
        $app = \Slim\Slim::getInstance();

        $credentials = array(
            'email'    => $app->request->post('email'),
            'password' => $app->request->post('password'),
        );

        $user = Sentry::authenticateAndRemember($credentials);

        $app->redirect('/admin/dashbord');

    }

    public function dashboard () {
        $app = \Slim\Slim::getInstance();

        $jobs        = Job::take(10)->get();
        $crawledJobs = CrawledJob::all();

        $app->render('static/header.php');
        $app->render('admin/dashboard.php', array (
            'jobs'        => $jobs,
            'crawledJobs' => $crawledJobs
        ));
        $app->render('static/footer.php');
    }

    public static function mustBeAuthenticated () {
        $app = \Slim\Slim::getInstance();

        if (!Sentry::check())
            $app->redirect('/admin');
    }
}
