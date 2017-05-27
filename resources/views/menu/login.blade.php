<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> login</a>
    <ul id="login-dp" class="dropdown-menu">
        <div class="row">
            <div class="col-md-12">
                <form>

                    <div class="form-group">
                        <input type="email" id="email" name="email" class="form-control" placeholder="email" required>
                    </div>

                    <div class="form-group">
                        <input type="password" id="password" class="form-control" placeholder="password" required>
                    </div>

                    <div class="form-group" hidden>
                        <div class="checkbox">
                            <label>
                                <input name="remember" type="checkbox">
                                Remember me
                            </label>
                        </div>
                    </div>

                    <div class="form-group">
                        <button type="submit" id="login" class="btn btn-primary btn-block">Login</button>
                    </div>

                </form>

                <div class="text-center alert alert-danger" role="alert" id="login-alert" hidden></div>

                <div class="form-group" hidden>
                    <div class="help-block text-right"><a href="/forgot">Forgot password?</a></div>
                </div>
            </div>
            <a href="{{ route ('showregister') }}">
                <div class="bottom text-center">Register</div>
            </a>
        </div>
    </ul>
</li>