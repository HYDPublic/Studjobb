<?php
class Deploy {

    public function pull () {
        $app = \Slim\Slim::getInstance();
        $payload = json_decode ($app->request->getBody(), true);
        echo shell_exec ('cd /var/www/studjobb/scripts && ./deploy.sh');
        echo shell_exec('whoami');
    }
}
