<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> my account</a>
    <ul id="login-dp" class="dropdown-menu">
        <div class="row">
            <div class="col-md-12">
                <form action="{{ route ('logout') }}" method="post">

                    <div class="form-group">
                        @if (!empty ($code->uri))
                            <input type="text" name="uri" value="{{ $code->uri }}" hidden>
                        @endif
                        <button type="submit" class="text-center btn btn-danger btn-block">Log out</button>
                    </div>

                </form>
            </div>
        </div>
    </ul>
</li>