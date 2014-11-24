<?php
class Mail {

    public function receive () {
        $app = \Slim\Slim::getInstance();

        /* Get the email address and the job id */
        $emailaddress = $app->request->get('emailaddress');
        $crawledJobId = $app->request->get('crawledJobId');

        if (empty($emailaddress) || empty($crawledJobId))
            throw new Exception ('Må ha en e-post og en tilhørende jobb-id.');

        /* Try to connect */
        $inbox = imap_open (
            $app->mailconfig['imap']['host'],
            $app->mailconfig['imap']['username'],
            $app->mailconfig['imap']['password']
        ) or die (imap_last_error());

        /* Grab emails by searching for the provided email */
        $emails = imap_search ($inbox,
            'ANSWERED '.
            'FROM "'.$emailaddress.'"'
        );

        /* Loop through each one */
        if ($emails) {
            foreach ($emails as $email) {

                /* Get information specific to this email */
                $overview  = imap_fetch_overview ($inbox, $email, 0);
                $structure = imap_fetchstructure ($inbox, $email);

                /* If encoding is provided, attempt to decode */
                if (isset($structure->encoding)) {
                    $message = imap_fetchbody ($inbox, $email, 1);

                    /* Decode the body correctly */
                    try {
                        if ($structure->encoding == 3
                        || (isset($structure->parts[0])
                        &&  $structure->parts[0]->encoding == 3))
                            $message = imap_base64 ($message);
                        else if ($structure->encoding == 1)
                            $message = imap_8bit   ($message);
                        else
                            $message = imap_qprint ($message);
                    } catch (Exception $e) {
                        $message = imap_fetchbody ($inbox, $email, 1);
                    }

                /* Use the raw body */
                } else {
                    $message = $message = imap_fetchbody ($inbox, $email, 1);
                }

                /* Check if unique message_id */
                if (Email::where('message_id', $overview[0]->message_id)->get() !== null) {

                    $emailToStore = new Email();

                    /* If no subject is provided */
                    if (isset($overview[0]->subject))
                        $emailToStore->subject = utf8_decode(imap_utf8($overview[0]->subject));

                    /* Fill in attributes */
                    $emailToStore->from       = $overview[0]->from;
                    $emailToStore->message_id = $overview[0]->message_id;
                    $emailToStore->body       = $message;
                    $emailToStore->sent_at    = date ('Y-m-d G:i:s', $overview[0]->udate);
                    $emailToStore->crawled_id = $crawledJobId;

                    /* Store the email */
                    $emailToStore->save();
                }
            }
        }

        /* Terminate the connection */
        imap_close ($inbox);

        /* Redirect back */
        $app->redirect('/admin/skrapt/' . $crawledJobId);

    }

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
