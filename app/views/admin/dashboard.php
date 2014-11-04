        <div id="dashboard" class="col-md-8 col-md-offset-2">

            <div class="intro">
                <h3>Dashbord</h3>
                <p>Dette er alle jobbene i systemet. Klikk for å redigere.</p>
                <table class="table table-hover table-jobs">
                    <tbody>
                        <?php foreach ($jobs as $job): ?>
                        <tr data-href="/admin/stilling/<?php print $job->id; ?>">
                            <td><strong><?php print $job->company->name; ?></strong></td>
                            <td><span class="badge badge-orange"><?php print $job->type; ?></span></td>
                            <td><span class="job-title"><?php print $job->title; ?></span></td>
                            <td><?php print $job->place; ?></td>
                            <td>Frist: <?php print $job->due(); ?></td>
                            <td><?php if ($job->published) print 'Publisert'; else print 'Upublisert'; ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>

                <h3>Selskaper</h3>
                <p>Dette er alle selskapene.</p>
                <table class="table table-hover table-jobs">
                    <tbody>
                        <?php foreach ($companies as $company): ?>
                        <tr data-href="/admin/selskap/<?php print $company->id; ?>">
                            <td><strong><?php print $company->name; ?></strong></td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>

                <h3>Skrapt</h3>
                <p>Dette er de skrapte jobbene.</p>
                <table class="table table-hover table-jobs">
                    <tbody>
                        <?php foreach ($crawledJobs as $crawledJob): ?>
                        <tr data-href="/admin/skrapt/<?php print $crawledJob->id; ?>"
                            class="<?php print strtolower($crawledJob->status); ?>">
                            <td><strong><?php print $crawledJob->company; ?></strong></td>
                            <td><?php print $crawledJob->source(); ?></td>
                            <td><?php print $crawledJob->title; ?></td>
                            <td><?php print $crawledJob->createdAt(); ?></td>
                            <td><?php print $crawledJob->status; ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
        </div>
