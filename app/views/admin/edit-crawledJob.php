        <div id="job" class="col-md-8 col-md-offset-2">

            <div class="intro col-md-12">

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
                    <select>
                        <option value="volvo">Ingenting</option>
                        <option value="volvo">Sendt mail</option>
                        <option value="volvo">Bestilt</option>
                        <option value="volvo">Sendt faktura</option>
                        <option value="volvo">Betalt</option>
                    </select>
                    <br/>

                    <label>Skrapt den: </label>
                    <span><?php print $crawledJob->createdAt(); ?></span>
                    <br/>

                    <label>Selskap: </label>
                    <span><?php print $crawledJob->company; ?></span>
                </p>

                <hr>

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

                        <div id="editor-container"></div>

                        <textarea id="buffer" name="content"></textarea>

                        <input type="submit" class="btn btn-custom-lighten" value="Publiser">
                    </form>

                </div>
            </div>

        </div>
