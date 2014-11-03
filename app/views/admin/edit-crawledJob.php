        <div id="job" class="col-md-8 col-md-offset-2">

            <div class="intro col-md-12">

                <p>
                    <a class="back" href="/admin/dashbord">← Tilbake til Dashbordet</a>
                </p>

                <h3><?php print $crawledJob->title; ?></h3>
                <p>
                    <a href="<?php print $crawledJob->url; ?>">
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
                </p>


                <hr>

                <div class="col-md-6">
                    <h4>Ta kontakt</h4>

                        <form>
                            <input type="text" class="form-control">
                        </form>

                </div>

                <div class="col-md-6">
                    <h4>Lag annonse</h4>

                    <form>
                        <input type="text" class="form-control">
                        <textarea class="form-control"></textarea>
                    </form>

                </div>
            </div>

        </div>
