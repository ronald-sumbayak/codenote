@extends ('base')

@section ('subtitle')
    {{ $code->uri }} (Syntax-Highlighted)
@endsection

@section ('styles')
    <link rel="stylesheet" href="/css/styles/default.css">
    <link rel="stylesheet" href="/css/styles/rainbow.css">
@endsection

@section ('content')


    <pre style="margin-top: 5%; width: 70%; margin-left: 15%;" ><code class="java" style="height:400px; text-align: left; width: 100%; ">{{ $code->source }}</code></pre>


       @include ('footer')
@endsection

@section ('scripts')
    <script src="/js/highlight.pack.js"></script>
    <script>
        hljs.tabReplace = '    ';
        hljs.initHighlightingOnLoad ();
    </script>
@endsection
