<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-lock"></i> Password</a>
    <ul id="login-dp" class="dropdown-menu">
        <div class="row">
            <div class="col-md-12">
                <form>
                @if ($code->password)

                    <input name="username" value="{{ $code->uri }}" hidden>

                    <div class="form-group">
                        <input id="old-password" class="form-control" type="password" placeholder="old password" required>
                    </div>

                    <div class="form-group">
                        <input id="new-password" class="form-control" type="password" placeholder="new password" required>
                    </div>

                    <div class="row">
                        <div class="form-group col-sm-6">
                            <button type="submit" id="set-password" class="btn btn-block btn-success">Change</button>
                        </div>

                        <div class="form-group col-sm-6">
                            <button id="clear-password" class="btn btn-block btn-danger">Remove Password</button>
                        </div>
                    </div>

                @else

                    <div class="form-group">
                        <input id="new-password" class="form-control" type="password" placeholder="new password" required>
                    </div>

                    <div class="form-group">
                        <button type="submit" id="set-password" class="btn btn-block btn-success">Set</button>
                    </div>

                @endif
                </form>

                <div class="alert alert-danger text-center" role="alert" id="set-password-alert" hidden></div>

            </div>
        </div>
    </ul>
</li>