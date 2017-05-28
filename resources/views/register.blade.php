<!doctype html>
<html>
<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="/img/favicon.png">
    <title>codenote | register</title>

    <link rel="stylesheet" href="/css/bootstrap.min.css">
    <link rel="stylesheet" href="/css/form.css">

</head>
<body style="">
    <style>
        body{
            background-image: url("/img/bg.png");
        }
    </style>

    <div class="container" style="margin-top: 12.5%;">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="panel panel-default">
                    <div class="panel-heading text-center"> <strong> REGISTER </strong></div>
                    <div class="panel-body" >
                        <form class="form-horizontal"  >

                            <div class="form-group text-center">
                                <div class="col-md-6 col-md-offset-3">
                                    <input id="name" type="text" class="form-control" name="name" value="" required autofocus placeholder="name">

                                </div>
                            </div>

                            <div class="form-group">
                                <div class="col-md-6 col-md-offset-3">
                                    <input id="email" type="email" class="form-control" name="email" value="" required placeholder="email">
                                </div>
                            </div>

                            <div class="form-group">
                                <div class="col-md-6 col-md-offset-3">
                                    <input id="password" type="password" class="form-control" name="password" required placeholder="password">
                                </div>
                            </div>

                            <div class="form-group">
                                <div class="col-md-6 col-md-offset-3">
                                    <input id="password-confirm" type="password" class="form-control" name="password_confirmation" required placeholder="confirm password">
                                </div>
                            </div>

                            <div class="form-group text-center">
                                <div class="col-md-6 col-md-offset-3">
                                    <button id="register" type="submit" class="btn btn-primary">
                                        Register
                                    </button>
                                </div>
                            </div>
                        </form>

                        <div class="text-center alert alert-danger" role="alert" id="register-alert" hidden></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="/js/jquery-3.2.1.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/code/register.js"></script>

</body>

</html>