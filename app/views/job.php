        <div id="job" class="col-md-8 col-md-offset-2">

            <div class="intro col-md-8">
                <h3><?php print $job->title; ?></h3>
                <div class="content">
                    <?php print $job->content; ?>
                </div>
            </div>

            <div class="company col-md-4 well">
                <img src="<?php print $job->company->logo; ?>" class="logo">
                <div class="about">
                    <p><?php print $job->company->about; ?></p>
                </div>
            </div>
        </div>
