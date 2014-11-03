<?php
class Admin {

    public function login () {
        $app = \Slim\Slim::getInstance();
        $app->render('header.php');
        $app->render('admin/login.php');
        $app->render('footer.php');
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
        $app->render('header.php');
        $app->render('admin/dashboard.php');
        $app->render('footer.php');
    }

    public static function mustBeAuthenticated () {
        $app = \Slim\Slim::getInstance();
        if (!Sentry::check())
            $app->redirect('/admin');
    }
}
