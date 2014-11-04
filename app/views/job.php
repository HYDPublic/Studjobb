        <div id="job" class="col-md-8 col-md-offset-2">

            <div class="intro col-md-10">
                <p>
                    <a class="back" href="/">← Tilbake til forsiden</a>
                <?php if (Sentry::check()): ?>
                    | <a class="back" href="/admin/stilling/<?php print $job->id; ?>">
                        Rediger
                      </a>
                <?php endif; ?>
                </p>

                <h3><?php print $job->title; ?></h3>

                <div class="company well">
                    <img src="<?php print $job->company->logo; ?>" class="logo">
                    <div class="about">
                        <p><?php print $job->company->about; ?></p>
                    </div>
                </div>

                <div class="content">
                    <?php print $job->content; ?>
                </div>
            </div>
        </div>
