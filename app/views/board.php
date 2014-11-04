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
                <div class="col-md-5 col-sm-10 col-xs-12">
                    <div class="left-inner-addon ">
                            <span class="glyphicon glyphicon-search orange"></span>
                            <input type="text" id="search" class="form-control"
                                placeholder="'sommerjobb', 'javascript', 'design' ...">
                    </div>
                </div>
                <div class="col-md-2 col-md-offset-4 hide-sm">
                    <button type="button" class="btn btn-custom-lighten">
                        Legg ut en stilling!
                    </button>
                </div>
            </div>

            <?php foreach ($categories as $category): ?>
                <div class="listing">
                    <h3><?php print $category->name; ?></h3>
                    <table class="table table-hover">
                        <tbody>
                            <?php foreach ($category->jobs as $job): ?>
                            <?php if ($job->published == true): ?>
                            <tr data-href="/stilling/<?php print $job->id; ?>">
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
                        <h4 class="modal-title">Uten jobb?</h4>
                    </div>
                    <div class="modal-body">
                        <p>
                            Hver mandag sender vi deg en e-post over de nyeste jobbene.
                            Du kan når som helst melde deg av. E-posten din blir aldri
                            delt med noen tredjeparter og vi sender deg maks èn e-post
                            i uka.
                        </p>

                        <form id="newsletter-form" method="post" action="/nyhetsbrev">
                            <div class="form-group">
                                <label>Din e-post</label>
                                <input type="email" class="form-control" placeholder="stud@ntnu.no">
                            </div>
                        </form>

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-custom-lighten">Meld meg på</button>
                    </div>
                </div>
            </div>
        </div>
