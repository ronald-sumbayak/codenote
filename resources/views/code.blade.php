@extends ('base')

@section ('subtitle')
    {{ $code->uri }} (Syntax-Highlighted)
@endsection

@section ('styles')
    <link rel="stylesheet" href="/css/styles/default.css">
    <link rel="stylesheet" href="/css/styles/github.com">
@endsection

@section ('content')


    <pre style="margin-top: 5%;"><code class="java" style="height:300px; ">{{ $code->source }}</code></pre>


       @include ('footer')
@endsection

@section ('scripts')
    <script src="/js/highlight.pack.js"></script>
    <script>
        hljs.tabReplace = '    ';
        hljs.initHighlightingOnLoad ();
    </script>
@endsection
