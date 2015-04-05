<?php

class SMS {
    
    public function send () {
        require __DIR__.'/../configuration.php';
        $app = \Slim\Slim::getInstance();

        $device = $configuration['pushbullet']['device']; 
        $telno    = $app->request->post('telno');  
        $smsbody  = $app->request->post('smsbody');
        $app->pushbullet->device($device)->sendSms($telno, $smsbody);

        $app->redirect('/admin/skrapt/'. $app->request->post('crawledJobId'));
    }
}
