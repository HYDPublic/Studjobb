<?php
class Mail {
    
    // Receives the post data from the admin panel 
    public function enqueue () {

        $app = \Slim\Slim::getInstance();
        
        /* Find the appropriate timestamp to send */
        $nextWeekday = function () {

            $today         = date('N');
            $dayToSend     = $today; 
            $hourToSend    = 12; 
            $minutesToSend = 50;
            $days          = array (
                'Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday'
            );
            
            // Is today a weekday? (Mon-Thu)
            if ($today > 0 /*Sun*/ && 5 /*Fri*/ > $today)
                
                // Are we past the preffered hour?
                if (date('H') > $hourToSend)
                    $dayToSend = $days[++$dayToSend]; 
            
                // Send it today then
                else
                    $dayToSend = $days[$dayToSend];    

            // Then it must be sent on wednesday 
             else
                $dayToSend = $days[3];
            
            // Generate the timestamp
            return strtotime($dayToSend . ' ' . $hourToSend . ':' . $minutesToSend); 
        };
 
        /* Mark status as 'Mailkø' */
        $crawledJob = CrawledJob::find($app->request->post('crawledJobId'));
        $crawledJob->status = 'Mailkø';
        $crawledJob->save();

        /* Store in mailqueue */
        $email = new Email();
        $email->crawled_job_id = $app->request->post('crawledJobId'); 
        $email->to           = $app->request->post('to'); 
        $email->name         = $app->request->post('name');
        $email->subject      = $app->request->post('subject');
        $email->body         = $app->request->post('body');
        $email->send_at      = date('Y-m-d H:i:s', $nextWeekday());
        $email->save();
    
        $app->redirect('/admin/skrapt/'. $app->request->post('crawledJobId') .
                       '?date='. date('Y-m-d-H:i', $nextWeekday()));
    }

    // Sends queued email by using SMTP
    public function send () {

        $app = \Slim\Slim::getInstance();

        // Must have a valid cron-token
        if ($app->request->get('token') !== $app->mailcron['token'])
            throw new Exception('Ugyldig mailcron token. Godt forsøk, det skal du ha!');

        // Set execution limit to 0 and timezone.
        date_default_timezone_set('Europe/Oslo');
        set_time_limit(0);
        
        /* Send all emails which has not been marked as sent */
        $queuedEmails = Email::where('sent', '=', 0)->get();
        
        /* Debugging output */
        echo "Found " . count($queuedEmails) . " mails in queue \n\n";
        
        foreach ($queuedEmails as $key => $queuedEmail) {
    
            // Marked the crawledjob as queued
            $crawledJob = CrawledJob::find($queuedEmail->crawled_job_id);

            if (strtotime($queuedEmail->send_at) <= time()) {
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

                $mail->addAddress($queuedEmail->to, $queuedEmail->name);
                $mail->Subject = $queuedEmail->subject;
                $mail->Body    = $queuedEmail->body;
                
                /* Mail-error */
                if (!$mail->send()) {
                    echo "Mailer Error: " . $mail->ErrorInfo . "\n<br>";

                /* Success: Email sent */
                } else {
                     
                    // Success
                    echo "Successfully delivered, apparently. \n";

                    // Mark email as sent 
                    $queuedEmail->sent = true;
                    $queuedEmail->save();
                    
                    // Mark crawledjob as contacted
                    $crawledJob->status = 'Kontaktet';
                    $crawledJob->email  = $queuedEmail->to;
                }
            }   
            
            // Save the crawledjob
            $crawledJob->save(); 
            
            // Delete the object
            $mail = null;

            // Sleep to avoid spam
            sleep(2 * $key);
        }
    }
}
