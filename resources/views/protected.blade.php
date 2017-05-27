<!doctype html>
<html>
<head>
    <title>codenote / {{ $code->uri }} [Password]</title>
    <link rel="stylesheet" href="/css/bootstrap.min.css">

    <style >
        body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6,
        pre, form, fieldset, input, textarea, p, blockquote, th, td {
            padding:0;
            margin:0;}

        fieldset, img {border:0}

        ol, ul, li {list-style:none}

        :focus {outline:none}

        body,
        input,
        textarea,
        select {
            font-family: 'Open Sans', sans-serif;
            font-size: 16px;
            color: #4c4c4c;
        }
        h1 {
            font-size: 32px;
            font-weight: 300;
            color: #4c4c4c;
            text-align: center;
            padding-top: 10px;
            margin-bottom: 10px;
        }

        html{
            background-color: #ffffff;
        }

        .testbox {
            margin: 15% auto 0 auto;
            width: 700px;
            height: 250px;
            -webkit-border-radius: 8px/7px;
            -moz-border-radius: 8px/7px;
            border-radius: 8px/7px;
            background-color: #ebebeb;
            -webkit-box-shadow: 1px 2px 5px rgba(0,0,0,.31);
            -moz-box-shadow: 1px 2px 5px rgba(0,0,0,.31);
            box-shadow: 1px 2px 5px rgba(0,0,0,.31);
            border: solid 1px #cbc9c9;
        }

    </style>
</head>

<body>
    <div class="testbox">
        <h3>Password</h3>
        <div style="margin-top: 8%;">password for <strong>{{ $code->uri }}</strong></div>

        <form>
            <input type="text" name="username" value="{{ $code->uri }}" hidden> <!-- ojok dihapus :v -->
            <input type="password" name="password" id="password" required style="margin-top: 3%;">
            <button id="check-password" type="submit" class="btn btn-success">Unlock</button>
        </form>

        <div class="alert alert-danger" role="alert" id="checkpassword-alert" hidden></div>
    </div>

    <script src="/js/jquery-3.2.1.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/code/password.js"></script>
    <!-- static variable -->
    <script>
    uri = '{{ $code->uri }}';
    </script>
</body>
</html>
