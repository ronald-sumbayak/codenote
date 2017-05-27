@extends ('base')

@section ('subtitle')
    {{ $code->uri }} (Syntax-Highlighted)
@endsection

@section ('styles')
    <link rel="stylesheet" href="/css/styles/default.css">
    <link rel="stylesheet" href="/css/styles/github.com">
@endsection

@section ('content')
    <pre><code class="java">{{ $code->source }}</code></pre>
@endsection

@section ('scripts')
    <script src="/js/highlight.pack.js"></script>
    <script>
        hljs.tabReplace = '    ';
        hljs.initHighlightingOnLoad ();
    </script>
@endsection
