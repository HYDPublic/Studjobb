

        <div id="board" class="col-md-8 col-md-offset-2 col-sm-12 col-xs-12">
            <div class="listing row">
                <h3>Søkeresultater</h3>
                <?php if (count($jobs) > 0): ?>
                <table class="table table-hover">
                    <tbody>
                    <?php foreach ($jobs as $job): ?>
                        <?php if ($job->published == true): ?>
                        <tr data-href="/stilling/<?php print $job->id; ?>" <?php if ($job->marked) print 'class="marked"'; ?>>
                            <td class="company"><strong><?php print $job->company->name; ?></strong></td>
                            <td class="type"><span class="badge badge-orange"><?php print $job->type; ?></span></td>
                            <td class="title"><span class="job-title"><?php print $job->title; ?></span></td>
                            <td class="place"><?php print $job->place; ?></td>
                            <td class="due timeago" title="<?php print $job->due(); ?>"></td>
                        </tr>
                        <?php endif; ?>
                    <?php endforeach; ?>
                    </tbody>
                </table>
                <?php else: ?>
                <p>Fant ingen resultater.</p>
                <?php endif; ?>
            </div>
        </div>
