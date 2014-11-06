<?php
class Mail {

    public function send () {
        $app = \Slim\Slim::getInstance();

        $mail = new PHPMailer;
        $mail->CharSet     = $app->mailconfig['charset'];
        $mail->isSMTP();
        $mail->SMTPDebug   = $app->mailconfig['smtpdebug'];
        $mail->Debugoutput = $app->mailconfig['debugoutput'];
        $mail->Host        = $app->mailconfig['host'];
        $mail->Port        = $app->mailconfig['port'];
        $mail->SMTPSecure  = $app->mailconfig['smtpsecure'];
        $mail->SMTPAuth    = $app->mailconfig['smtpauth'];
        $mail->Username    = $app->mailconfig['username'];
        $mail->Password    = $app->mailconfig['password'];
        $mail->setFrom      ($app->mailconfig['from'], $app->mailconfig['fromName']);
        $mail->addReplyTo   ($app->mailconfig['from'], $app->mailconfig['fromName']);

        $mail->addAddress($app->request->post('to'), $app->request->post('name'));
        $mail->Subject = $app->request->post('subject');
        $mail->Body    = $app->request->post('body');

        if (!$mail->send()) {
            echo "Mailer Error: " . $mail->ErrorInfo;
        } else {
            echo "Message sent!";

            $crawledJob = CrawledJob::find($app->request->post('crawledJobId'));
            $crawledJob->status = 'Kontaktet';
            $crawledJob->save();
        }
    }
}
