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
        print $fields;
        $app->render('static/header.php');
        $app->render('submit/form.php');
        $app->render('static/footer.php');
    }

    public function submitJob () {
        $app      = \Slim\Slim::getInstance();
        $storage  = new \Upload\Storage\FileSystem($app->logo['upload-dir']);
        $errors   = array  ();

        if (!strstr($app->request->post('email'), '@'))
            $errors['email'] = 'Du må ha en gyldig e-post.';

        if (strlen($app->request->post('title')) < 5
        || strlen($app->request->post('title')) > 140)
            $errors['title'] = 'Tittelen er for lang eller for kort.';

        if (!$app->request->post('company'))
            $errors['company'] = 'Selskapet må ha et navn.';

        if (!$app->request->post('uploaded')) {
            $logo     = new \Upload\File('logo', $storage);
            $filename = uniqid ();
            $logo->setName($filename);
            $logo->addValidations(array(
                new \Upload\Validation\Mimetype(array(
                    'image/png',
                    'image/gif',
                    'image/jpg'
                ))
            ));

            try {
                $logo->upload();
                $uploaded = true;
            } catch (\Exception $e) {
                $errors['logo'] = $logo->getErrors();
                $uploaded = false;
            }
        } else {
            $uploaded = true;
            $filename = $app->request->post('uploaded');
        }

        $app->render('static/header.php');

        if (empty($errors)) {

            $job = new SubmittedJob();
            $job->title   = $app->request->post('title');
            $job->email   = $app->request->post('email');
            $job->content = $app->request->post('content');
            $job->company = $app->request->post('company');
            $job->logo    = $app->request->post('logo');
            $job->place   = $app->request->post('place');
            $job->mark    = $app->request->post('mark');
            $job->save();

            $app->render('submit/thanks.php');

        } else {
            $app->render('submit/form.php', array (
                'fields'   => $app->request->post(),
                'errors'   => $errors,
                'uploaded' => $uploaded,
                'filename' => $filename
            ));
        }

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
