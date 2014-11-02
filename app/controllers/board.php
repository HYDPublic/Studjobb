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

        $x = Job::find(1);

        print_r($x);
    }
}
