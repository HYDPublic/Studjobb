

        <div id="board" class="col-md-8 col-md-offset-2 col-sm-12 col-xs-12">
            <div class="row">
                <div class="intro">
                    <p>
                        <strong>Studjobb.no</strong> er for studenter som ønsker
                        å finne jobb, startups og oppdrag. Kom i kontakt med bedrifter
                        som ønsker å ansette studenter!
                    </p>
                    <p>
                        <strong>Ikke gå glipp av drømmejobben!</strong> Hver torsdag
                        sender vi deg aktuelle stillinger på e-post. Gjør som 200 andre studenter og
                        <a href="#" data-toggle="modal" data-target="#newsletter"><strong>klikk her</strong></a> for å
                        melde deg på! <!--Du kan også følge <a href="//twitter.com/studjobb">@Studjobb</a>
                        på <i class="fa fa-twitter"></i>-->
                    </p>
                </div>
            </div>

            <form method="get" action="/finn">
                <div class="search well row">
                    <div class="col-md-6 col-sm-12">
                        <div class="left-inner-addon ">
                                <span class="glyphicon glyphicon-search orange"></span>
                                <input type="text" name="q" id="search" class="form-control"
                                    placeholder="'sommerjobb', 'javascript', 'design' ...">
                        </div>
                    </div>
                    <div class="col-md-6 col-sm-12">
                        <a href="/utlys">
                            <button type="button" class="btn btn-custom-lighten hidden-xs" style="width:100%">
                                Legg ut stilling for 1500,- i 30 dager!
                            </button>
                        </a>
                    </div>
                </div>
            </form>


            <?php foreach ($categories as $category): ?>
                    <div class="listing row">
                        <h3><?php print $category->name; ?></h3>
                        <table class="table table-hover">
                            <thead>
								<th>Selskap</th>
								<th>Type</th>
								<th>Stilling</th>
								<th>Sted</th>
								<th>Søknadsfrist</th>
							</thead>

                            <tbody>
                                <?php foreach ($category->jobs as $job): ?>
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
                    </div>

            <?php endforeach; ?>
        </div>

        <div class="modal fade" id="newsletter" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                        <h4 class="modal-title">På utkikk etter jobb? Gjør som 200 andre studenter!</h4>
                    </div>
                    <form class="form-horizontal" role="form" id="newsletter-form" method="post" action="/nyhetsbrev">
                    <div class="modal-body">

                        <p>
                            Hver onsdag sender vi deg en oversikt over de nyeste jobbene.
                            Du kan når som helst frabe deg den ukentlig oversikten. E-postadressen din
                            blir aldri delt med noen tredjeparter og vi sender deg maks èn oversikt
                            i uka.
                        </p>

                        <div class="form-group">
                            <label for="email" class="col-sm-2 control-label">E-post</label>
                            <div class="col-sm-10">
                                <input type="email" name="email" class="form-control" placeholder="ola.nordmann@ntnu.no" required>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="school" class="col-sm-2 control-label">Skole</label>
                            <div class="col-sm-10">
                                <select name="school">
                                <?php foreach ($schools as $school): ?>
                                    <option value="<?php print $school->id; ?>">
                                        <?php print $school->name; ?>
                                    </option>
                                <?php endforeach; ?>
                            </select>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">Lukk</button>
                        <button type="submit" id="signup" class="btn btn-custom-lighten">Meld meg på</button>
                    </div>
                    </form>
                </div>
            </div>
        </div>
