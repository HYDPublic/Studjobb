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

    public static function error (\Exception $e) {
        $app = \Slim\Slim::getInstance();
		print_r($e);
        $app->render('static/header.php');
        $app->render('static/error.php', array ('message' => $e->getMessage()));
        $app->render('static/footer.php');
    }
}
