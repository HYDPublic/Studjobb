        <div id="job" class="col-md-8 col-md-offset-2">

            <div class="intro col-md-10">
                <p>
                    <a class="back" href="/admin/dashbord">← Tilbake til Dashbordet</a>
                </p>

                <form id="update-job" method="post">

                    <div class="form-group">
                        <label>Tittel</label>
                        <input type="text" name="title" class="form-control"
                            value="<?php print $job->title; ?>">
                    </div>

                    <div class="form-group">
                        <label>Publisert</label>
                        <input name="published" type="checkbox" <?php if ($job->published == 1) print 'checked'; ?>>
                    </div>

                    <div class="form-group">
                        <label>Sted</label>
                        <input name="place" type="text" value="<?php print $job->place; ?>"
                            class="form-control">
                    </div>

                    <div class="form-group">
                        <label>Selskap</label>
                        <select name="company">
                            <?php foreach ($companies as $company): ?>
                            <option value="<?php print $company->id; ?>"
                                <?php if ($job->company == $company) print 'selected'; ?>>
                                <?php print $company->name; ?>
                            </option>
                            <?php endforeach; ?>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Type jobb</label>
                        <input name="type" type="text" value="<?php print $job->type; ?>"
                        placeholder="deltid, heltid, sommerjobb" class="form-control">
                    </div>

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

                    <div id="editor-container"><?php print $job->content; ?></div>

                    <textarea id="buffer" name="content"></textarea>

                    <input type="submit" class="btn btn-custom-lighten" value="Lagre">
                </form>
            </div>

        </div>
