<?php
class Newsletter {

    public function thanks () {
        $app = \Slim\Slim::getInstance();

        $app->render('static/header.php');
        $app->render('newsletter/thanks.php');
        $app->render('static/footer.php');
    }
}
