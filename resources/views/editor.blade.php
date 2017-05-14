<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>codenote | {{ $code->uri }}</title>
    <link rel="stylesheet" href="css/font-awesome.min.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:600italic,400,800,700,300' rel='stylesheet' type='text/css'>
</head>

<body>
    <!-- ====================================================
	header section -->
    <header class="top-header">
        <div class="container">
            <div class="row header-row">
                <div class="col-md-12">
                    <nav class="navbar navbar-default">
                        <img src="img/logo.png" alt="" class="logo">
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
                                    <li><a href="/">New Note</a></li>
                                    <li><button id="open-password">Password</button></li>
                                    <li><button id="open-changeuri">change URL</button></li>
                                </ul>
                            </div>
                        </div>
                    </nav>
                </div>
            </div>
        </div>
    </header>

    <section class="banner text-center" id="sec1">
        <div id="changeuri-form" hidden>
            <input type="text" name="newuri" id="new-uri" value="{{ $code->uri }}" required>
            <button onclick="changeuri ()">Change</button>
            <button>Cancel</button>
            <div class="alert alert-danger" role="alert" id="changeuri-alert" hidden></div>
        </div>

        <div id="password-form" hidden>
            @if ($code->password)
                <input type="password" name="oldpassword" id="old-password" required>
                <input type="password" name="newpassword" id="new-password" required>
                <button onclick="change_password ()">Set Password</button>
                <button onclick="clear_password ()">Clear Password</button>
            @else
                <input type="password" name="newpassword" id="new-password" required>
                <button onclick="change_password ()">Set Password</button>
            @endif
            <button>Cancel</button>
            <div class="alert alert-danger" role="alert" id="setpassword-alert" hidden></div>
        </div>



        <div class="col-sm-12">
            <div class="container">
                <code><textarea class="form-control code-form" rows="20" id="sourceCode">{{ $code->source }}</textarea></code>
                <code><textarea class="form-control code-form" rows="10" style="margin-top: 0;" id="input"></textarea></code>
                <div class="alert alert-success compilation-alert" role="alert" id="success-alert" hidden></div>
                <div class="alert alert-danger compilation-alert" role="alert" id="error-alert" hidden></div>
                <div class="alert alert-info compilation-alert" role="alert" id="stderr-alert" hidden></div>
                <code><div class="alert alert-warning compilation-alert" role="alert" id="cmpinfo-alert" hidden></div></code>
                <code><div class="form-control" style="margin-top: 0;" id="output"></div></code>

                <div class="form-group row col-xs-2">
                    <select class="form-control code-form" id="lang">
                        <option value="0" selected>Text</option>
                    </select>
                </div>

                <button class="code-form"vonclick="run ()" id="run">Run</button>
            </div>
        </div>



    </section>

    <!-- script tags -->
    <script src="js/jquery-2.1.1.js"></script>
    <script src="js/smoothscroll.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/custom.js"></script>

    <!-- koneksi ke bek en -->
    <script src="js/code/sync.js"></script>
    <script src="js/code/compile.js"></script>
    <script src="js/code/editor.js"></script>
    <script src="js/code/password.js"></script>
    <script src="js/code/sphere.js"></script>
    <script src="js/code/uri.js"></script>

    <!-- static variable -->
    <script>
    uri = '{{ $code->uri }}';
    caret = {{ $code->caret }};
    lastupdate = '{{ $code->updated_at }}';
    timer = setTimeout (function () {}, 0);
    </script>
</body>

</html>
