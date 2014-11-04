<?php
class Newsletter {

    public function signup () {
        $app = \Slim\Slim::getInstance();

        $result = $app->mailchimp->call('lists/subscribe', array(
            'id'                => '9e391988e0',
            'email'             => array (
                'email'=>'michael@studjobb.no'
            ),
            'merge_vars'        => array (
                'FNAME'     => 'Davy',
                'LNAME'     => 'Jones',
                'EDUCATION' => 'NTNU'
            ),
            'double_optin'      => false,
            'update_existing'   => true,
            'replace_interests' => false,
            'send_welcome'      => false,
        ));

        print_r($result);
    }

    public function thanks () {
        $app = \Slim\Slim::getInstance();

        $app->render('static/header.php');
        $app->render('newsletter/thanks.php');
        $app->render('static/footer.php');
    }
}
