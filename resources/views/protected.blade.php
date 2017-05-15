<!doctype html>
<html>
<head>
    <title>codenote / {{ $code->uri }} [Password]</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
</head>

<body>
    <div>
        <div>password for {{ $code->uri }}</div>
        <input type="text" name="username" value="{{ $code->uri }}" hidden> <!-- ojok dihapus :v -->
        <input type="password" name="password" id="password" required>
        <button onclick="check_password ()">Submit</button>
        <div class="alert alert-danger" role="alert" id="checkpassword-alert" hidden></div>
    </div>

    <script src="js/jquery-2.1.1.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/sync.js"></script>
    <!-- static variable --> <script>
    uri = '{{ $code->uri }}';
    </script>
</body>
</html>
