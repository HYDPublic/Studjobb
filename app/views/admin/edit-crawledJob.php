        <div id="job" class="col-md-8 col-md-offset-2">

            <div class="intro col-md-12">
                <div class="row">
                    <div class="col-md-10">
                        <p>
                            <a class="back" href="/admin/dashbord">
                                ← Tilbake til Dashbordet
                            </a>
                        </p>
                        <p>
                            <a href="<?php print $crawledJob->url; ?>" target="_blank">
                                <strong>Besøk kilden</strong>
                                <span class="glyphicon glyphicon-share-alt"></span>
                            </a>
                        </p>
                        <p>
                            <form method="post" action="/admin/skrapt/<?php print $crawledJob->id; ?>/status">
                                <label>Status: </label>
                                <?php $statuses = array ('Ingen', 'Kontaktet', 'Bestilt', 'Laget'); ?>
                                <select name="status">
                                    <?php foreach ($statuses as $status): ?>
                                    <option value="<?php print $status; ?>"
                                        <?php if ($crawledJob->status == $status) print 'selected'; ?>>
                                        <?php print $status; ?>
                                    </option>
                                    <?php endforeach; ?>
                                </select>
                                <br/>
                                <input type="submit" class="btn btn-custom-lighten" value="Oppdater status">
                            </form>

                            <br/>

                            <label>Skrapt den: </label>
                            <span><?php print $crawledJob->createdAt(); ?></span>
                            <br/>

                            <label>Selskap: </label>
                            <span><?php print $crawledJob->company; ?></span>
                        </p>
                    </div>
                </div>

                <hr>

                <div class="row">
                    <h3>Send e-post</h3>
                    <div class="col-md-10">
                        <form id="mail" method="post" action="/admin/mail">
                            <input type="text" name="to" class="form-control" placeholder="E-post"
                                value="<?php print trim($crawledJob->getEmail()); ?>">
                            <input type="text" name="name" class="form-control" placeholder="Navn">
                            <input type="text" name="subject" class="form-control" value="Utlysning på Studjobb.no">
                            <textarea class="form-control" name="body"><?php print $mailtext; ?></textarea>
                            <br/>
                            <input type="hidden" name="crawledJobId" value="<?php print $crawledJob->id; ?>">
                            <input type="submit" class="btn btn-custom-lighten" value="Send mail">
                        </form>
                    </div>
                </div>

                <hr>

                <div class="row">
                    <h3>Selskap</h3>
                    <div class="col-md-10">

                        <form id="update-job" action="/admin/selskap/ny" method="post">

                            <div class="form-group">
                                <label>Tittel</label>
                                <input type="text" name="name" class="form-control">
                            </div>

                            <div class="form-group">
                                <label>Logo</label>
                                <input type="text" name="logo" class="form-control">
                            </div>

                            <div class="form-group">
                                <label>Om selskapet</label>
                                <textarea name="about" class="form-control"></textarea>
                            </div>


                            <input type="submit" class="btn btn-custom-lighten" value="Lagre">
                        </form>
                    </div>
                </div>

                <hr>

                <div class="row">
                    <h3>Utlysning</h3>
                    <div class="col-md-10">
                        <form id="update-job" method="post" action="/admin/stilling">
                            <input type="hidden" name="crawledJobId" value="<?php print $crawledJob->id; ?>"

                            <label>Tittel</label>
                            <input type="text" name="title" class="form-control" value="<?php print $crawledJob->title; ?>">

                            <label>Søknadsfrist</label>
                            <input type="text" name="due" class="form-control" value="2015-11-05">

                            <div id="formatting-container">
                                <select title="Size" class="ql-size">
                                    <option value="10px">Small</option>
                                    <option value="13px" selected>Normal</option>
                                    <option value="18px">Large</option>
                                    <option value="32px">Huge</option>
                                </select>

                                <button type="button" class="btn ql-bold">Bold</button>
                                <button type="button" class="btn ql-italic">Italic</button>
                                <button type="button" class="btn ql-underline">Under</button>
                                <button type="button" class="btn ql-strike">Strike</button>
                                <button type="button" class="btn ql-link">Link</button>
                                <button type="button" class="btn ql-image">Image</button>
                                <button type="button" class="btn ql-bullet">Bullet</button>
                                <button type="button" class="btn ql-list">List</button>
                            </div>

                            <div id="editor-container"><?php print strip_tags($crawledJob->content,
                                '<a><p><br><b><i><ul><li><img><ol><em><h1><h2><h3><h4><strong>'); ?></div>

                            <textarea id="buffer" name="content"></textarea>

                            <input type="submit" class="btn btn-custom-lighten" value="Publiser">
                        </form>

                    </div>
                </div>
            </div>
        </div>
