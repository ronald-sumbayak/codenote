<!doctype html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="img/favicon.png">
    <title>codenote | @yield ('subtitle')</title>

    <link rel="stylesheet" href="/css/bootstrap.min.css">
    <link rel="stylesheet" href="/css/font-awesome.min.css">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/style2.css">

    @yield ('styles')

</head>

<body>
    @include ('header')

    <section class="banner text-center">

        @yield ('content')
    </section>

    {{--@include ('footer')--}}

    <!-- script tags -->
    <script src="/js/jquery-3.2.1.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/smoothscroll.js"></script>
    <script src="/js/ie.js"></script>

    @yield ('scripts')

</body>
</html>