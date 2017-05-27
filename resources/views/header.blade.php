<header class="top-header">
    <div class="container">
        <div class="row header-row">
            <div class="col-md-12">
                <nav class="navbar navbar-default">
                    <img src="/img/logo2.png" alt="" class="logo" style="margin-top: 5px;">
                    <div class="container-fluid">
                        <div class="navbar-header">
                            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>
                        </div>
                        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul class="nav navbar-nav navbar-right">

                                @yield ('navbar-content')

                            </ul>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </div>
</header>