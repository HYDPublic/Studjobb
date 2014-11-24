<?php
class Deploy {

    public function pull () {
        $app = \Slim\Slim::getInstance();
        $payload = json_decode ($app->request->getBody(), true);
        shell_exec ('cd /var/www/studjobb; git fetch --all; git reset --hard origin/development');
    }
}
