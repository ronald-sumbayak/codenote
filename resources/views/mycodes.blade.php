@extends ('base')

@section ('subtitle')
    {{ Auth::user ()->name }}
@endsection

@section ('navbar-content')
    <li><a href="/">new note</a></li>
    @include ('menu.account')
@endsection

@section ('content')
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-9 col-md-12 col-lg-12">

                {{--
                jangan pake bulk dulu wkw
                --}}
                {{--<div class="pull-left">--}}

                    {{--<div class="btn-group" role="group">--}}
                        {{--<button id="select-all" class="btn btn-default">All</button>--}}
                        {{--<button id="select-all" class="btn btn-default">None</button>--}}
                    {{--</div>--}}

                    {{--<button class="btn btn-default" id="delete">--}}
                        {{--<i class="fa fa-trash"></i>--}}
                    {{--</button>--}}

                {{--</div>--}}

                <div class="pull-right">
                    {{ $codes->links () }}
                </div>
            </div>
        </div>

        <div class="row" style="margin-top: 4%;">
            <div class="col-xs-12 col-sm-9 col-md-12 col-lg-12">
                <div role="tabpanel">

                        <div role="tabpanel" class="tab-pane active" id="home">

                            <table class="table">
                                <tbody  >

                                @foreach ($codes as $code)
                                    <tr>
                                        {{--<td scope="row">--}}
                                            {{--<input type="checkbox"/>--}}
                                        {{--</td>--}}
                                        <td ><a href="/{{$code->uri}}" style="float: left; margin-top: 3%;">{{ $code->uri }}</a></td>

                                        <td>
                                            {{ $code->langName }} {{ $code->langVersion }} 
                                        </td>

                                        <td>
                                            @if ($code->password)
                                                <form action="{{ route ('clearpassword') }}" method="post">
                                                    <input type="text" name="uri" value="{{ $code->uri }}" hidden>
                                                    <button type="submit" class="btn btn-link"><i class="fa fa-unlock"></i></button>
                                                </form>
                                            @endif
                                        </td>

                                        <td>
                                            <a href="/raw/{{ $code->uri }}" target="_blank"><i class="fa fa-eye" style="padding: 0 3px; "></i></a>
                                            <a href="/code/{{ $code->uri }}" target="_blank"><i class="fa fa-code"  style="padding: 0 3px;"></i></a>
                                            <a href="/download/{{ $code->uri }}"><i class="fa fa-download"  style="padding: 0 3px;"></i></a>
                                        </td>

                                        <td>
                                             

                                            <form action="{{ route ('delete') }}" method="post">
                                                <input type="text" name="uri" value="{{ $code->uri }}" hidden>
                                                <button type="submit" class="btn btn-link" ><i class="fa fa-trash-o"></i></button>
                                            </form>

                                        </td>
                                    </tr>
                                @endforeach

                                </tbody>
                            </table>
                        </div>
                </div>
            </div>
        </div>
    </div>


    @include ('footer')
@endsection