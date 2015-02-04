        <div id="dashboard" class="col-md-12">

            <div class="intro">

                <div class="row">

                    <div class="col-md-6">
                    <h3>Dashbord</h3>
                    <h4>Medlemmer på nyhetsbrevet: <?php print $count; ?></h4>
                    </div>
                    <div class="col-md-6">
                        <img src="http://piwik.littlist.no/index.php?module=API&method=ImageGraph.get&idSite=<?php print $piwikSiteid; ?>&apiModule=VisitsSummary&apiAction=get&token_auth=<?php print $piwikToken; ?>&graphType=evolution&period=day&date=previous30&width=500&height=250'"

                    </div>
                </div>

                <hr>

                <div class="row">
                    <div class="col-md-6">
                        <h3>Jobber i systemet</h3>
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
                    </div>

                    <div class="col-md-4 col-md-offset-2">
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
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-6">
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

                    <div class="col-md-4 col-md-offset-2">
                        <h3>Innsendt</h3>
                        <p>Dette er de innsendte jobbene.</p>
                    </div>

                </div>
            </div>
        </div>
