<?php
class Deploy {

    public function pull () {
        $app = \Slim\Slim::getInstance();

        $sign = substr($app->request->headers->get('X-Hub-Signature'), 5);
		$hmac = hash_hmac('sha1', $app->request->getBody(), $app->github['deployKey']);
		if ($sign == $hmac)
            echo 'Signed!!' . $app->request->headers->get('X-Hub-Signature');
        else
            echo "not signed";

        $payload = json_decode ($app->request->getBody(), true);
        echo shell_exec ('cd /var/www/studjobb/scripts && ./deploy.sh');
        echo shell_exec('whoami');


    }
}
