        <div id="board" class="col-md-8 col-md-offset-2">

            <div class="intro">
                <p>
                    <strong>Studjobb.no</strong> er for studenter som ønsker
                    å finne jobb, startups og oppdrag. Kom i kontakt med bedrifter
                    som ønsker å ansette studenter!
                </p>
                <p>
                    <strong>Ikke gå glipp av drømmejobben!</strong> Hver mandag
                    sender vi deg aktuelle stillinger på e-post. Klikk her for å
                    melde deg på! Du kan også følge <a href="//twitter.com/studjobb">@Studjobb</a>
                    på <i class="fa fa-twitter"></i>
                </p>
            </div>

            <div class="search well col-md-12">
                <div class="col-md-5 col-xs-12">
                    <div class="left-inner-addon ">
                            <span class="glyphicon glyphicon-search orange"></span>
                            <input type="text" id="search" class="form-control"
                                placeholder="'sommerjobb', 'javascript', 'design' ...">
                        </div>
                </div>
                <div class="col-md-2 col-md-offset-4">
                    <button type="button" class="btn btn-custom-lighten">
                        Legg ut en stilling!
                    </button>
                </div>
            </div>

            <div class="listing">

                <h3>Webutvikling</h3>

                <table class="table table-hover">
                    <tbody>
                        <?php foreach ($jobs as $job): ?>
                        <tr data-href="/stilling/1">
                            <td><strong><?php print $job->company->name; ?></strong></td>
                            <td><span class="badge badge-orange"><?php print $job->type; ?></span></td>
                            <td><span class="job-title"><?php print $job->title; ?></span></td>
                            <td><?php print $job->place; ?></td>
                            <td>Frist: <?php print $job->due(); ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
        </div>
