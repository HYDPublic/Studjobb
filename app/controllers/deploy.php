<?php
class Deploy {

    public function pull () {
        $app = \Slim\Slim::getInstance();
        $payload = json_decode ($app->request->getBody(), true);
        echo shell_exec ('cd /var/www/studjobb && git fetch --all && git reset --hard origin/development');
        echo shell_exec('whoami');
    }
}
