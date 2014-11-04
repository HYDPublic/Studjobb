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

        $companies = Company::all();
        $job       = Job::find((int) $id);
        if (!$job)
            throw new Exception ('Fant ingen stilling.');

        $app->render('static/header.php');
        $app->render('admin/edit-job.php', array (
            'job'       => $job,
            'companies' => $companies
        ));
        $app->render('static/footer.php');
    }

    public function company ($id) {
        $app = \Slim\Slim::getInstance();

        $company = Company::find($id);
        if (!$company)
            throw new Exception ('Fant ingen selskap.');

        $app->render('static/header.php');
        $app->render('admin/edit-company.php', array (
            'company' => $company
        ));
        $app->render('static/footer.php');
    }

    public function updateCompany ($id) {
        $app = \Slim\Slim::getInstance();

        $company = Company::find($id);
        $company->name     = $app->request->post('name');
        $company->about    = $app->request->post('about');
        $company->logo     = $app->request->post('logo');
        $company->save();

        $app->redirect('/admin/selskap/' . $id);
    }

    public function updateCrawledJob ($id) {
        $app = \Slim\Slim::getInstance();

        $company = CrawledJob::find($id);
        $company->status     = $app->request->post('status');
        $company->save();

        $app->redirect('/admin/skrapt/' . $id);
    }


    public function updateJob ($id) {
        $app = \Slim\Slim::getInstance();

        $job = Job::find($id);
        $job->title      = $app->request->post('title');
        $job->content    = $app->request->post('content');
        $job->type       = $app->request->post('type');
        $job->company_id = $app->request->post('company');
        $job->place      = $app->request->post('place');

        if ($app->request->post('published') == 'on')
            $job->published = true;
        else
            $job->published = false;
        $job->save();

        $app->redirect('/admin/stilling/' . $id);
    }

    public function createJob () {
        $app = \Slim\Slim::getInstance();

        $job = new Job();
        $job->title = $app->request->post('title');
        $job->content = $app->request->post('content');
        $job->save();

        $app->redirect('/admin/stilling/' . $job->id);
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
        $companies   = Company::all();

        $app->render('static/header.php');
        $app->render('admin/dashboard.php', array (
            'jobs'        => $jobs,
            'companies'   => $companies,
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
