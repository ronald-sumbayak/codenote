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
                                    <li><a type="button" id="open-password" style="cursor:pointer">Password</a></li>
                                    <li><a type="button" id="open-changeuri" style="cursor:pointer" data-toggle="modal" data-target=".bd-example-modal-lg">change URL</a></li>
                                </ul>
                            </div>
                        </div>
                    </nav>
                </div>
            </div>
        </div>
    </header>

    <section class="banner text-center" id="sec1" style="margin-top: 1%;">
        <div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg" >
            <div class="modal-content">
                 <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Change URL</h5>
                  </div>
                <div class="modal-body">
              <div id="changeuri-form">
                    <input type="text" name="newuri" id="new-uri" value="{{ $code->uri }}" required>
                        <button onclick="changeuri ()" class="code-form btn btn-success">Change</button>
                        <button class="code-form btn btn-success" data-dismiss="modal" id="butcan">Cancel</button>
                        <div class="alert alert-danger" role="alert" id="changeuri-alert" hidden></div>
                </div>
                </div>
            </div>
          </div>
        </div>

        <!-- <div id="changeuri-form" hidden>
            <input type="text" name="newuri" id="new-uri" value="{{ $code->uri }}" required>
            <button onclick="changeuri ()">Change</button>
            <button>Cancel</button>
            <div class="alert alert-danger" role="alert" id="changeuri-alert" hidden></div>
        </div> -->

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
                <textarea class="form-control code-form" rows="20" id="sourceCode">{{ $code->source }}</textarea>
                <textarea class="form-control code-form open-input" rows="10" style="margin-top: 5%; display: none;" id="input" ></textarea>
                <div class="alert alert-success compilation-alert" role="alert" id="success-alert" hidden></div>
                <div class="alert alert-danger compilation-alert" role="alert" id="error-alert" hidden></div>
                <div class="alert alert-info compilation-alert" role="alert" id="stderr-alert" hidden></div>
                <div class="alert alert-warning compilation-alert" role="alert" id="cmpinfo-alert" hidden></div>
                <div class="form-control" id="output"></div>

                <div>
                    <div class="form-group row col-xs-2">
                        <select class="form-control code-form" id="lang">
                            <option value="0" selected>Text</option>
                        </select>
                    </div>

                    <button class="code-form btn btn-success" id="open-test" style="float: left;">Input</button>
                    <button class="code-form btn btn-success" onclick="run ()" id="run" style="float: right;">Run</button>
                </div>
            </div>
        </div>

        <div class="col-sm-12 footer">
            
            <p> Presents By KERJA.IN </p>
            <p> CODENOTE is powered By BadutEngine </p>

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
    <script src="js/code/input.js"></script>
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
