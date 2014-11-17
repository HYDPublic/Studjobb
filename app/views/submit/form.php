

        <div id="board" class="col-md-8 col-md-offset-2 col-sm-12 col-xs-12">
            <div class="row">
                <div class="intro">
                    <blockquote>
                        Annonsen din vil være synlig på forsiden i 30 dager. I tillegg
                        vil den sendes med nyhetsbrevet den førstkommende torsdagen. Prisen
                        for en annonse er 250,-. Annonsering er derimot gratis for start-ups.
                    </blockquote>
                </div>
            </div>
            <h3>Vennligst send utlysninger til <a href="mailto:michael@studjobb.no">michael@studjobb.no</a></h3>
            <form id="submit" class="form-horizontal" role="form" method="post" enctype="multipart/form-data" style="display:none;">
                <legend>Steg 1: Stillingen</legend>
                <div class="form-group">

                    <label class="col-sm-2 control-label">Stillingstittel</label>
                    <div class="col-sm-8">

                        <input type="text" required name="title" class="form-control" value="<?php if (isset($fields['title'])) print $fields['title']; ?>">
                        <?php if(isset($errors['title'])): ?>
                            <div class="alert alert-danger" role="alert"><?php print $errors['title']; ?></div>
                        <?php endif; ?>
                        <p class="help-block">For eksempel 'systemutvikler', 'trainee' eller 'sommerjobb'.</p>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-sm-2 control-label">Sted</label>
                    <div class="col-sm-8">
                        <input type="text" required name="place" class="form-control" <?php if (isset($fields['place'])) print $fields['place']; ?>>
                        <?php if(isset($errors['place'])): ?>
                            <div class="alert alert-danger" role="alert"><?php print $errors['place']; ?></div>
                        <?php endif; ?>
                        <p class="help-block">Hvor i landet gjelder stillingen?</p>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-sm-2 control-label">Beskrivelse</label>
                    <div class="col-sm-8">
                        <div id="formatting-container">
                            <button type="button" class="btn ql-bold">Fet</button>
                            <button type="button" class="btn ql-italic">Kursiv</button>
                            <button type="button" class="btn ql-underline">Understrek</button>
                            <button type="button" class="btn ql-link">Lenke</button>
                            <button type="button" class="btn ql-bullet">Liste</button>
                        </div>
                        <div id="editor-container"><?php if (isset($fields['content'])) print $fields['content']; ?></div>
                        <textarea name="content" id="buffer" style="hidden"></textarea>
                        <?php if(isset($errors['content'])): ?>
                            <div class="alert alert-danger" role="alert"><?php print $errors['content']; ?></div>
                        <?php endif; ?>
                        <p class="help-block">
                            Selve stillingsbeskrivelsen. Husk å skrive hvordan
                            man skal søke og hvem man skal ta kontakt med.
                        </p>
                    </div>
                </div>

                <legend>Steg 2: Selskapet</legend>
                <div class="form-group">
                    <label class="col-sm-2 control-label">Navn</label>
                    <div class="col-sm-8">
                        <input type="text" required name="company" class="form-control" value="<?php if (isset($fields['company'])) print $fields['company']; ?>">
                        <?php if(isset($errors['company'])): ?>
                            <div class="alert alert-danger" role="alert"><?php print $errors['company']; ?></div>
                        <?php endif; ?>
                        <p class="help-block">Navn på selskapet.</p>
                    </div>
                </div>

                <?php if ($uploaded == false): ?>
                <div class="form-group">
                    <label class="col-sm-2 control-label">Logo</label>
                    <div class="col-sm-8">
                        <input type="file" required name="logo">
                        <?php if(isset($errors['logo'])): ?>
                            <div class="alert alert-danger" role="alert"><?php if (isset($fields['logo'])) print $errors['logo']; ?></div>
                        <?php endif; ?>
                        <p class="help-block">Last opp et bilde av logoen.</p>
                    </div>
                </div>
                <?php else: ?>
                    <input type="hidden" required name="uploaded" value="<?php print $filename; ?>">
                <?php endif; ?>

                <div class="form-group">
                    <label class="col-sm-2 control-label">Om selskapet</label>
                    <div class="col-sm-8">
                        <textarea type="text" required name="about" class="form-control"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-sm-2 control-label">E-post</label>
                    <div class="col-sm-8">
                        <input type="email" required name="email" class="form-control" value="<?php if (isset($fields['email'])) print $fields['email']; ?>">
                        <?php if(isset($errors['email'])): ?>
                            <div class="alert alert-danger" role="alert"><?php print $errors['email']; ?></div>
                        <?php endif; ?>
                        <p class="help-block">Faktura og kvittering sendes til denne adressen.</p>
                    </div>
                </div>

                <legend>Gjør annonsen synligere</legend>
                <div class="form-group">

                    <label for="mark" class="col-sm-2 control-label">Uthev</label>
                    <div class="col-sm-4">
                        <input id="mark" type="checkbox" name="mark"> Ja, takk
                        <p class="help-block">Uthevede annonser får flere klikk. Det koster bare <strong>100,-</strong> ekstra.</p>
                    </div>
                    <div class="col-sm-6">
                        <img src="/img/marked.jpg">
                    </div>
                </div>

                <div class="form-group">
                    <div class="col-sm-6 col-sm-offset-2">
                        <button type="submit" id="buy" class="btn btn-custom-lighten" style="width:100%">
                            Kjøp
                        </button>
                    </div>
                </div>

            </form>
        </div>
