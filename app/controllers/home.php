<?php
class Home {

    public function about () {
        $app = \Slim\Slim::getInstance();
        $app->render('static/header.php');
        $app->render('static/about.php');
        $app->render('static/footer.php');
    }

    public function contact () {

    }

    public static function notFound () {
        $app = \Slim\Slim::getInstance();
        $app->render('static/header.php');
        $app->render('static/notFound.php');
        $app->render('static/footer.php');
    }

}
