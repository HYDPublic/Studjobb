

        <div id="board" class="col-md-8 col-md-offset-2 col-sm-12 col-xs-12">
            <div class="row">
                <div class="intro">
                    <blockquote>
                        Annonsen din vil være synlig på forsiden i 30 dager. I tillegg
                        vil den sendes med nyhetsbrevet den førstkommende mandagen. Prisen
                        for en annonse er 250,-. Annonsering er derimot gratis for start-ups.
                    </blockquote>
                </div>
            </div>

            <form id="submit" class="form-horizontal" role="form" method="post">
                <legend>Steg 1: Stillingen</legend>
                <div class="form-group">
                    <label class="col-sm-2 control-label">Stillingstittel</label>
                    <div class="col-sm-8">
                        <input type="text" name="title" class="form-control">
                        <p class="help-block">For eksempel 'systemutvikler', 'trainee' eller 'sommerjobb'.</p>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-sm-2 control-label">Sted</label>
                    <div class="col-sm-8">
                        <input type="text" name="text" class="form-control">
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
                        <div id="editor-container"></div>
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
                        <input type="text" name="company" class="form-control">
                        <p class="help-block">Navn på selskapet.</p>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-sm-2 control-label">Logo</label>
                    <div class="col-sm-8">
                        <input type="file" name="logo">
                        <p class="help-block">Last opp et bilde av logoen.</p>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-sm-2 control-label">Om selskapet</label>
                    <div class="col-sm-8">
                        <textarea type="text" name="about" class="form-control"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-sm-2 control-label">E-post</label>
                    <div class="col-sm-8">
                        <input type="text" name="email" class="form-control">
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
