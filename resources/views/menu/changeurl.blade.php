<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-link"></i> Change URL</a>
    <ul id="login-dp" class="dropdown-menu">
        <div class="row">
            <div class="col-md-12">
                <form>
                    <div class="form-group">
                        <div class="input-group">
                            <span class="input-group-addon">codenotes.me/</span>
                            <input type="text" name="newuri" class="form-control" id="new-uri" placeholder="url" value="{{ $code->uri }}" required>
                        </div>
                        <button type="submit" id="changeuri" class="btn btn-success btn-block" disabled style="margin-top: 10px;">Change</button>
                    </div>

                </form>

                <div class="text-center alert alert-danger" role="alert" id="changeuri-alert" hidden></div>
            </div>
        </div>
    </ul>
</li>