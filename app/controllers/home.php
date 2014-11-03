<?php
class Home {

    public function about () {
        $app = \Slim\Slim::getInstance();
        $app->render('header.php');
        $app->render('about.php');
        $app->render('footer.php');
    }

    public function contact () {

    }

    public static function notFound () {
        $app = \Slim\Slim::getInstance();
        $app->render('header.php');
        $app->render('notFound.php');
        $app->render('footer.php');
    }

}
