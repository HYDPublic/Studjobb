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
                            <label>Status: </label>
                            <form method="post" action="/admin/skrapt/<?php print $crawledJob->id; ?>/status">
                            <?php $statuses = array ('Kontaktet', 'Bestilt'); ?>
                            <select>
                                <?php foreach ($statuses as $status): ?>
                                <option value="<?php print $status; ?>"
                                    <?php if ($crawledJob->status == $status) print 'selected'; ?>>
                                    <?php print $status; ?>
                                </option>
                                <?php endforeach; ?>
                            </select>
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
                                value="<?php print $crawledJob->contact; ?>">
                            <input type="text" name="name" class="form-control" placeholder="Navn">
                            <input type="text" name="subject" class="form-control" value="Utlysning på Studjobb.no">
                            <textarea class="form-control" name="body"></textarea>
                            <br/>
                            <input type="submit" class="btn btn-custom-lighten" value="Send mail">
                        </form>
                    </div>
                </div>

                <hr>

                <div class="row">
                    <h3>Utlysning</h3>
                    <div class="col-md-10">
                        <form id="update-job" method="post" action="/admin/stilling">
                            <input type="text" name="title" class="form-control" value="<?php print $crawledJob->title; ?>">

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

                            <div id="editor-container"><?php print $crawledJob->content; ?></div>

                            <textarea id="buffer" name="content"></textarea>

                            <input type="submit" class="btn btn-custom-lighten" value="Publiser">
                        </form>

                    </div>
                </div>
            </div>
        </div>
