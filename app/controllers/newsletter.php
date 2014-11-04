<?php
class Newsletter {

    public function signup () {
        $app = \Slim\Slim::getInstance();

        $school = School::find($app->request->post('school'));
        if ($school->get()->isEmpty())
            throw new Exception ('Ugyldig skole.');

        $query = $app->mailchimp->call('lists/subscribe', array(
            'id'                => '9e391988e0',
            'email'             => array (
                'email' =>  $app->request->post('email')
            ),

            'merge_vars'        => array (
                'EDUCATION' => $school->name
            ),

            'double_optin'      => false,
            'update_existing'   => true,
            'replace_interests' => false,
            'send_welcome'      => true,
        ));

        if (isset($query['status']) && $query['status'] == 'error')
            throw new Exception ($query['error']);

        $app->redirect('/takk');
    }

    public function thanks () {
        $app = \Slim\Slim::getInstance();

        $app->render('static/header.php');
        $app->render('newsletter/thanks.php');
        $app->render('static/footer.php');
    }
}
