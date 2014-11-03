        <div id="job" class="col-md-8 col-md-offset-2">

            <div class="intro col-md-10">
                <p>
                    <a class="back" href="/admin/dashbord">← Tilbake til Dashbordet</a>
                </p>

                <form id="update-job" method="post">

                    <div class="form-group">
                        <label>Tittel</label>
                        <input type="text" name="name" class="form-control"
                            value="<?php print $company->name; ?>">
                    </div>

                    <div class="form-group">
                        <label>Logo</label>
                        <input type="text" name="logo" class="form-control"
                            value="<?php print $company->logo; ?>">
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

                    <div id="editor-container"><?php print $company->about; ?></div>

                    <textarea id="buffer" name="about"></textarea>

                    <input type="submit" class="btn btn-custom-lighten" value="Lagre">
                </form>
            </div>

        </div>
