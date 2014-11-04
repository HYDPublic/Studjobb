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

        $mail->addAddress('michaedm@stud.ntnu.no', 'Michael McMillan');

        $mail->Subject = 'Utlysning på Studjobb.no';
        $mail->Body    = 'Liten test :)';

        if (!$mail->send()) {
            echo "Mailer Error: " . $mail->ErrorInfo;
        } else {
            echo "Message sent!";
        }
    }
}
