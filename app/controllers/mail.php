<?php
class Mail {

    public function send () {
        $app = \Slim\Slim::getInstance();

        $mail = new PHPMailer;
        $mail->CharSet     = $app->mailconfig['smtp']['charset'];
        $mail->isSMTP();
        $mail->SMTPDebug   = $app->mailconfig['smtp']['smtpdebug'];
        $mail->Debugoutput = $app->mailconfig['smtp']['debugoutput'];
        $mail->Host        = $app->mailconfig['smtp']['host'];
        $mail->Port        = $app->mailconfig['smtp']['port'];
        $mail->SMTPSecure  = $app->mailconfig['smtp']['smtpsecure'];
        $mail->SMTPAuth    = $app->mailconfig['smtp']['smtpauth'];
        $mail->Username    = $app->mailconfig['smtp']['username'];
        $mail->Password    = $app->mailconfig['smtp']['password'];
        $mail->setFrom      ($app->mailconfig['smtp']['from'], $app->mailconfig['smtp']['fromName']);
        $mail->addReplyTo   ($app->mailconfig['smtp']['from'], $app->mailconfig['smtp']['fromName']);

        $mail->addAddress($app->request->post('to'), $app->request->post('name'));
        $mail->Subject = $app->request->post('subject');
        $mail->Body    = $app->request->post('body');

        if (!$mail->send()) {
            echo "Mailer Error: " . $mail->ErrorInfo;
        } else {
            $crawledJob = CrawledJob::find($app->request->post('crawledJobId'));
            $crawledJob->status = 'Kontaktet';
            $crawledJob->email  = $app->request->post('to');
            $crawledJob->save();

            $app->redirect('/admin/skrapt/' . $app->request->post('crawledJobId'));
        }
    }
}
